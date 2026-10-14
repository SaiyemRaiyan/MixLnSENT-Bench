"""Generate publication-ready figure for XAI prompt feature ablations.

Produces a multi-panel chart illustrating:
1. Accuracy Deltas with 95% Confidence Intervals across all ablations.
2. Hallucinated 'Mixed' percentage rates highlighting the Guardrail function.
3. Statistical significance under the Tri-Partite Architectural Taxonomy.
"""

import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SUMMARY_FILE = PROJECT_ROOT / "outputs" / "prompting" / "sentmix3l" / "results" / "xai_ablation_qwen_qwen3.8-27b.json"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "xai" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot():
    if not SUMMARY_FILE.exists():
        print(f"Error: {SUMMARY_FILE} not found.")
        return

    data = json.loads(SUMMARY_FILE.read_text(encoding="utf-8"))
    base_key = "zero_shot_v1"
    
    conditions = [
        ("zero_shot_ablate_drop_mixed_def_v1", "Drop Mixed Def\n(Definitions)", "redundant"),
        ("zero_shot_ablate_drop_rule1_v1", "Drop Rule 1\n(Bilingual)", "redundant"),
        ("zero_shot_ablate_drop_rule2_v1", "Drop Rule 2\n(Lexicon)", "redundant"),
        ("zero_shot_ablate_drop_rule3_v1", "Drop Rule 3\n(Context)", "shield"),
        ("zero_shot_ablate_drop_rule4_v1", "Drop Rule 4\n(Strict Mixed)", "guardrail"),
        ("zero_shot_ablate_drop_rule5_v1", "Drop Rule 5\n(Neutral Fallback)", "guardrail"),
        ("zero_shot_ablate_drop_rule6_v1", "Drop Rule 6\n(Sarcasm)", "guardrail"),
        ("zero_shot_ablate_drop_rule7_v1", "Drop Rule 7\n(Punctuation)", "guardrail"),
    ]

    labels = [c[1] for c in conditions]
    types = [c[2] for c in conditions]
    
    delta_acc = [data[c[0]]["delta_acc"] * 100 for c in conditions]
    err_low = [(data[c[0]]["delta_acc"] - data[c[0]]["stats"]["ci95"][0]) * 100 for c in conditions]
    err_high = [(data[c[0]]["stats"]["ci95"][1] - data[c[0]]["delta_acc"]) * 100 for c in conditions]
    inv_rates = [data[c[0]]["invalid_rate"] * 100 for c in conditions]
    base_inv = data[base_key]["invalid_rate"] * 100

    # Colors: Green for Redundant (drop improves), Orange for Shield, Crimson for Guardrail
    color_map = {
        "redundant": "#2E7D32",   # Forest Green
        "shield": "#F57C00",      # Amber/Orange
        "guardrail": "#C62828",   # Crimson Red
    }
    bar_colors = [color_map[t] for t in types]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
    plt.subplots_adjust(wspace=0.28, bottom=0.18)

    # Panel 1: Accuracy Delta with 95% CI
    y_pos = np.arange(len(conditions))
    ax1.axvline(0, color="black", linestyle="--", linewidth=1.0, alpha=0.7)
    
    bars1 = ax1.barh(y_pos, delta_acc, xerr=[err_low, err_high], color=bar_colors, alpha=0.85,
                     edgecolor="black", height=0.65, capsize=4)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=10, fontweight="medium")
    ax1.invert_yaxis()
    ax1.set_xlabel("Accuracy Delta vs Full Baseline (%)", fontsize=11, fontweight="bold")
    ax1.set_title("Panel A: Impact of Component Ablation on Accuracy\n(with 95% Paired CI)", fontsize=12, fontweight="bold")
    ax1.grid(axis="x", linestyle=":", alpha=0.6)

    # Annotate statistical significance
    for i, c in enumerate(conditions):
        p_val = data[c[0]]["stats"]["holm_p"]
        val = delta_acc[i]
        offset = 0.25 if val >= 0 else -0.35
        ha = "left" if val >= 0 else "right"
        sig_marker = "***" if p_val < 0.001 else ("*" if p_val < 0.05 else "")
        ax1.text(val + offset, i, f"{val:+.2f}% {sig_marker}", va="center", ha=ha, fontsize=9, fontweight="bold")

    # Panel 2: Invalid Hallucinated Mixed Rate
    bars2 = ax2.barh(y_pos, inv_rates, color=bar_colors, alpha=0.85, edgecolor="black", height=0.65)
    ax2.axvline(base_inv, color="blue", linestyle="--", linewidth=1.5, label=f"Baseline Rate ({base_inv:.1f}%)")
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([])
    ax2.invert_yaxis()
    ax2.set_xlabel("Hallucinated 'Mixed' Predictions (%)", fontsize=11, fontweight="bold")
    ax2.set_title("Panel B: Hallucinated 'Mixed' Rate on 3-Class Corpus\n(Ground Truth contains 0 Mixed)", fontsize=12, fontweight="bold")
    ax2.grid(axis="x", linestyle=":", alpha=0.6)
    ax2.legend(loc="lower right", frameon=True, fontsize=10)

    for i, val in enumerate(inv_rates):
        d_inv = val - base_inv
        ax2.text(val + 0.3, i, f"{val:.1f}% ({d_inv:+.1f}%)", va="center", fontsize=9, fontweight="bold")

    # Add custom legend for Taxonomy
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#2E7D32", edgecolor="black", label="Redundant / Distractive (Drop improves Acc)"),
        Patch(facecolor="#F57C00", edgecolor="black", label="Contextual Shield (Drop causes mild loss)"),
        Patch(facecolor="#C62828", edgecolor="black", label="Disambiguation Guardrail (Drop causes collapse, p < 1e-4)"),
    ]
    fig.legend(handles=legend_elements, loc="lower center", bbox_to_anchor=(0.5, 0.02),
               ncol=3, frameon=True, fontsize=10)

    out_path = OUTPUT_DIR / "fig_prompt_ablation_tripartite.png"
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print(f"Publication chart successfully saved to: {out_path}")


if __name__ == "__main__":
    plot()
