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


def plot_single(summary_file, output_name, model_title):
    if not summary_file.exists():
        print(f"Error: {summary_file} not found.")
        return

    data = json.loads(summary_file.read_text(encoding="utf-8"))
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
    
    ax1.barh(y_pos, delta_acc, xerr=[err_low, err_high], color=bar_colors, alpha=0.85,
             edgecolor="black", height=0.65, capsize=4)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=10, fontweight="medium")
    ax1.invert_yaxis()
    ax1.set_xlabel("Accuracy Delta vs Full Baseline (%)", fontsize=11, fontweight="bold")
    ax1.set_title(f"Panel A: Impact on Accuracy ({model_title})\n(with 95% Paired CI)", fontsize=12, fontweight="bold")
    ax1.grid(axis="x", linestyle=":", alpha=0.6)

    for i, c in enumerate(conditions):
        p_val = data[c[0]]["stats"].get("holm_p", 1.0)
        val = delta_acc[i]
        offset = 0.25 if val >= 0 else -0.35
        ha = "left" if val >= 0 else "right"
        sig_marker = "***" if p_val < 0.001 else ("*" if p_val < 0.05 else "")
        ax1.text(val + offset, i, f"{val:+.2f}% {sig_marker}", va="center", ha=ha, fontsize=9, fontweight="bold")

    # Panel 2: Invalid Hallucinated Mixed Rate
    ax2.barh(y_pos, inv_rates, color=bar_colors, alpha=0.85, edgecolor="black", height=0.65)
    ax2.axvline(base_inv, color="blue", linestyle="--", linewidth=1.5, label=f"Baseline Rate ({base_inv:.1f}%)")
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([])
    ax2.invert_yaxis()
    ax2.set_xlabel("Hallucinated 'Mixed' Predictions (%)", fontsize=11, fontweight="bold")
    ax2.set_title(f"Panel B: Hallucinated 'Mixed' Rate ({model_title})\n(Ground Truth contains 0 Mixed)", fontsize=12, fontweight="bold")
    ax2.grid(axis="x", linestyle=":", alpha=0.6)
    ax2.legend(loc="lower right", frameon=True, fontsize=10)

    for i, val in enumerate(inv_rates):
        d_inv = val - base_inv
        ax2.text(val + 0.3, i, f"{val:.1f}% ({d_inv:+.1f}%)", va="center", fontsize=9, fontweight="bold")

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#2E7D32", edgecolor="black", label="Redundant / Distractive (Drop improves Acc)"),
        Patch(facecolor="#F57C00", edgecolor="black", label="Contextual Shield (Drop causes mild loss)"),
        Patch(facecolor="#C62828", edgecolor="black", label="Disambiguation Guardrail (Drop causes collapse)"),
    ]
    fig.legend(handles=legend_elements, loc="lower center", bbox_to_anchor=(0.5, 0.02),
               ncol=3, frameon=True, fontsize=10)

    out_path = OUTPUT_DIR / output_name
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out_path}")


def plot_cross_model():
    qwen_file = PROJECT_ROOT / "outputs" / "prompting" / "sentmix3l" / "results" / "xai_ablation_qwen_qwen3.8-27b.json"
    gpt_file = PROJECT_ROOT / "outputs" / "prompting" / "sentmix3l" / "results" / "xai_ablation_openai_gpt-oss-20b.json"

    if not qwen_file.exists() or not gpt_file.exists():
        print("Both Qwen and GPT summary files are required for cross-model plot.")
        return

    qwen = json.loads(qwen_file.read_text(encoding="utf-8"))
    gpt = json.loads(gpt_file.read_text(encoding="utf-8"))

    conditions = [
        ("zero_shot_ablate_drop_mixed_def_v1", "Drop Mixed Def"),
        ("zero_shot_ablate_drop_rule1_v1", "Drop Rule 1 (Bilingual)"),
        ("zero_shot_ablate_drop_rule2_v1", "Drop Rule 2 (Lexicon)"),
        ("zero_shot_ablate_drop_rule3_v1", "Drop Rule 3 (Context)"),
        ("zero_shot_ablate_drop_rule4_v1", "Drop Rule 4 (Strict Mixed)"),
        ("zero_shot_ablate_drop_rule5_v1", "Drop Rule 5 (Neutral Fallback)"),
        ("zero_shot_ablate_drop_rule6_v1", "Drop Rule 6 (Sarcasm)"),
        ("zero_shot_ablate_drop_rule7_v1", "Drop Rule 7 (Punctuation)"),
    ]

    labels = [c[1] for c in conditions]
    y_pos = np.arange(len(conditions))
    height = 0.35

    qwen_acc = [qwen[c[0]]["delta_acc"] * 100 for c in conditions]
    gpt_acc = [gpt[c[0]]["delta_acc"] * 100 for c in conditions]

    qwen_inv = [(qwen[c[0]]["invalid_rate"] - qwen["zero_shot_v1"]["invalid_rate"]) * 100 for c in conditions]
    gpt_inv = [(gpt[c[0]]["invalid_rate"] - gpt["zero_shot_v1"]["invalid_rate"]) * 100 for c in conditions]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5), dpi=300)
    plt.subplots_adjust(wspace=0.28, bottom=0.15)

    # Panel A: Accuracy Deltas Comparison
    ax1.axvline(0, color="black", linestyle="--", linewidth=1.0, alpha=0.7)
    ax1.barh(y_pos - height/2, qwen_acc, height=height, label="Qwen 27B", color="#5C6BC0", edgecolor="black", alpha=0.85)
    ax1.barh(y_pos + height/2, gpt_acc, height=height, label="GPT-OSS-20B", color="#26A69A", edgecolor="black", alpha=0.85)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=10, fontweight="medium")
    ax1.invert_yaxis()
    ax1.set_xlabel("Accuracy Delta vs Baseline (%)", fontsize=11, fontweight="bold")
    ax1.set_title("Panel A: Cross-Model Accuracy Delta\n(Qwen 27B vs GPT-OSS-20B)", fontsize=12, fontweight="bold")
    ax1.grid(axis="x", linestyle=":", alpha=0.6)
    ax1.legend(loc="lower right", frameon=True, fontsize=10)

    # Panel B: Delta Hallucinated Mixed Comparison
    ax2.axvline(0, color="black", linestyle="--", linewidth=1.0, alpha=0.7)
    ax2.barh(y_pos - height/2, qwen_inv, height=height, label="Qwen 27B", color="#5C6BC0", edgecolor="black", alpha=0.85)
    ax2.barh(y_pos + height/2, gpt_inv, height=height, label="GPT-OSS-20B", color="#26A69A", edgecolor="black", alpha=0.85)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([])
    ax2.invert_yaxis()
    ax2.set_xlabel("Delta in Hallucinated 'Mixed' (%)", fontsize=11, fontweight="bold")
    ax2.set_title("Panel B: Cross-Model Shift in Hallucinated 'Mixed'\n(Negative values indicate reduced hallucination)", fontsize=12, fontweight="bold")
    ax2.grid(axis="x", linestyle=":", alpha=0.6)
    ax2.legend(loc="upper right", frameon=True, fontsize=10)

    out_path = OUTPUT_DIR / "fig_prompt_ablation_cross_model.png"
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out_path}")


def main():
    qwen_summary = PROJECT_ROOT / "outputs" / "prompting" / "sentmix3l" / "results" / "xai_ablation_qwen_qwen3.8-27b.json"
    gpt_summary = PROJECT_ROOT / "outputs" / "prompting" / "sentmix3l" / "results" / "xai_ablation_openai_gpt-oss-20b.json"

    plot_single(qwen_summary, "fig_prompt_ablation_tripartite.png", "Qwen 27B")
    plot_single(gpt_summary, "fig_prompt_ablation_gpt_oss_20b.png", "GPT-OSS-20B")
    plot_cross_model()


if __name__ == "__main__":
    main()

