

##  Repository Guide & Reproducibility Verification


| Path | Purpose & Contents |
|---|---|
| `data/` | Raw and preprocessed CSVs for `bnsentmix` and `sentmix3l`. |
| `prompts/prompting/` | Verbatim text prompts: `zero_shot_v1.txt`, `zero_shot_minimal_v1.txt`, `two_shot_v1.txt`, `five_shot_v1.txt`, `batch_format_v1.txt`, and micro-ablation variants. |
| `src/common/` | Dataset descriptors, scope resolvers (`config.py`, `datasets.py`, `metrics.py`). |
| `src/prompting/` | Core inference pipeline, API key rotation, provider wrappers (`runner.py`, `providers.py`). |
| `src/audit/` | Audit scripts for charts, shot curves, and ablation analysis (`xai_analysis.py`, `run_xai_ablation.py`). |
| `outputs/prompting/` | Full raw JSONL model prediction files across all models and conditions. |
| `outputs/xai/` | XAI evaluation outputs: `dev_gate.json`, `REPORT.md`, attribution tables, and Shapley logs. |
| `outputs/BnSentMix_XAI_Full_Research_Report.pdf` | Companion compiled publication PDF report. |

### How to Reproduce
1. Activate virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
2. Verify XAI gates:
   ```powershell
   python -m src.audit.xai_analysis
   ```
3. Run or inspect coverage:
   ```powershell
   python -m src.audit.coverage test
   ```
4. Generate updated publication charts:
   ```powershell
   python -m src.audit.charts test
   ```

---
*End of Research Monograph. Prepared for research paper integration.*
