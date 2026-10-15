# Frozen XAI preregistration

This file is generated from the frozen sample manifest, config, prompts, and git state.

```json
{
  "version": 1,
  "commit": "599662c5394278aad1b087f05e74dfa91ea179ea",
  "seed": 42,
  "sample_manifest": {
    "seed": 42,
    "split_seed": 42,
    "max_tokens": 30,
    "test_source_rows": 3003,
    "xai800": {
      "file": "samples\\xai800.jsonl",
      "sha256": "04c75d51a72bc2193d692e8c581a7f4f2371a3248532d391759e36f3b0c95353",
      "rows": 800,
      "class_counts": {
        "0": 200,
        "1": 200,
        "2": 200,
        "3": 200
      },
      "source": "fixed stratified test split",
      "eligible_excluded_fraction": 0.042957,
      "eligible_rows_before_class_cap": 2874,
      "rows_not_sampled_after_class_cap": 2074,
      "duplicate_summary": {
        "rows": 20015,
        "unique_normalized": 19753,
        "duplicate_groups": 258,
        "rows_in_duplicate_groups": 520,
        "conflict_groups": 19,
        "rows_in_conflict_groups": 38
      }
    },
    "xai200": {
      "file": "samples\\xai200.jsonl",
      "sha256": "fcfc9fa9da5c96d53f48893ae858d54d38407052caaba194857e136e0d2fac37",
      "rows": 200,
      "class_counts": {
        "0": 50,
        "1": 50,
        "2": 50,
        "3": 50
      },
      "source": "seeded subset of xai800"
    },
    "gemini300": {
      "file": "samples\\gemini300.jsonl",
      "sha256": "56acce35a82f5d6740b6895624126471a16fa41b6d69bd332a668790b76301e9",
      "rows": 300,
      "class_counts": {
        "0": 75,
        "1": 75,
        "2": 75,
        "3": 75
      },
      "source": "seeded subset of xai800"
    },
    "gemini_noise100": {
      "file": "samples\\gemini_noise100.jsonl",
      "sha256": "f88bd7ca433af82f44d77d6c1aec2156a1f32f9290f369923cbff36e84e64543",
      "rows": 100,
      "class_counts": {
        "0": 25,
        "1": 25,
        "2": 25,
        "3": 25
      },
      "source": "seeded subset of xai800"
    },
    "dev": {
      "file": "samples\\dev.jsonl",
      "sha256": "50cedb2142c313c1e658abeeb049cfd57444c06f853eb97573152aefa6591570",
      "rows": 585,
      "class_counts": {
        "0": 155,
        "1": 177,
        "2": 200,
        "3": 53
      },
      "source": "filtered 600-row train-only dev set plus extra train neutral rows for planted-cue validation",
      "extra_neutral_rows": 5
    }
  },
  "models": {
    "full_analysis": [
      {
        "provider": "groq",
        "model": "qwen/qwen3.8-27b"
      },
      {
        "provider": "groq",
        "model": "openai/gpt-oss-20b"
      }
    ],
    "restricted": {
      "provider": "commandcode",
      "model": "google/gemini-3.8-flash"
    }
  },
  "primary_prompt": "prompts/prompting/zero_shot_minimal_v1.txt",
  "hashed_files": {
    "outputs\\xai\\samples\\xai800.jsonl": "264e37168941f68a88b8e16a30952a74dca844fadfb65600776328cac69a01cd",
    "outputs\\xai\\samples\\xai200.jsonl": "ccc6d182586682160701774fb764447ae25ab69a5c4c13d1f7059410add192b9",
    "outputs\\xai\\samples\\gemini300.jsonl": "b3445555808811a61c0ddc129176f5d5f7830d756c142b7b0fea145898d57ef1",
    "outputs\\xai\\samples\\gemini_noise100.jsonl": "a40b7a8d12b66f179feb79e8a4970249bbdb35d8ee15e79ea454037cadf02012",
    "outputs\\xai\\samples\\dev.jsonl": "cc6204ee57beb49bebdcf8d8ca5adfd3cf87c108371b077fe6930f2d41fae694",
    "outputs\\xai\\samples\\manifest.json": "bba199cfbf4b2e6934ce08dc96542d568b37f278a185f03a56951f198d2d2a38",
    "prompts\\prompting\\batch_format_v1.txt": "03dc237e769911c2ef2fc5d03644752f38a2403e1b1b5688a1e098c6b00f0a04",
    "prompts\\prompting\\five_shot_minimal_v1.txt": "cc6fee2b8191296b7fc92029721df6e823c41404749219ecf9c32a61a41e72eb",
    "prompts\\prompting\\zero_shot_ablate_drop_mixed_def_v1.txt": "3279a436d5199ff8aba062afd694f01351acff4e41bede39197b2e7409429c7c",
    "prompts\\prompting\\zero_shot_ablate_drop_rule1_v1.txt": "6d2bf3c08beecbd4a4c3b4b631cf2084dd3bf4b5fa2c6fb8dde5416e2d5eea63",
    "prompts\\prompting\\zero_shot_ablate_drop_rule2_v1.txt": "cdaf2ba5a27f0077bf24174ff83b25d6871567288883ffa100b887390451e56e",
    "prompts\\prompting\\zero_shot_ablate_drop_rule3_v1.txt": "a8e44907be84ee05a5d90e2829678b17df5e3b82140694f0d2387dccf8826da3",
    "prompts\\prompting\\zero_shot_ablate_drop_rule4_v1.txt": "f45b6001f8ff5129f750e090f39bc3984a7098d259a7d6bcf368b98d82d5c92f",
    "prompts\\prompting\\zero_shot_ablate_drop_rule5_v1.txt": "65b08aacc8b30ae667ba97d2407f2b4d30ec9c10c41369756d5f1ad84ec685a5",
    "prompts\\prompting\\zero_shot_ablate_drop_rule6_v1.txt": "5f266bc86ea7b0d96100be7cc40a0cb6d608801c8e27e39974b053f4aa281938",
    "prompts\\prompting\\zero_shot_ablate_drop_rule7_v1.txt": "52ac1c9715a3c832c7365aee227895264aef24c708a651d5f1369408c58d2c2e",
    "prompts\\prompting\\zero_shot_minimal_v1.txt": "3d2bd947121dd714577e9b52eacda84fdd28e9a075134775d7a19c03cf0122f6",
    "prompts\\prompting\\zero_shot_v1.txt": "3e7a17354116fa945fb9caf0188de4f8da3860528f6bedfaff6221651c44e215",
    "prompts\\xai\\five_shot_minimal_leave_out_01_v1.txt": "c0f795472112ee686d912f9e214df7464798e24973d85d4c2cdccb3ae3597ef2",
    "prompts\\xai\\five_shot_minimal_leave_out_02_v1.txt": "b992ef1728e1030323043b7332a63ee9ba03deba0a8f77b39911e370cea2b415",
    "prompts\\xai\\five_shot_minimal_leave_out_03_v1.txt": "fee6c288e9fb0b011abbaa5704523caa2ae26a7a14ce702158f97b1fbcc34927",
    "prompts\\xai\\five_shot_minimal_leave_out_04_v1.txt": "317f66c9f4cf5cad95db4c81fa82acc52cb64b61b59f13761a403577c4526a1b",
    "prompts\\xai\\five_shot_minimal_leave_out_05_v1.txt": "3416ed8ba35320ec42a33d67b949b3fd570aade3954bbed8b402d8f61aad004e",
    "prompts\\xai\\five_shot_minimal_leave_out_06_v1.txt": "64e47d14b52c491d7d01d2a4439ddf0276ba3829bd6b02991b8d2bbcb5858fcf",
    "prompts\\xai\\five_shot_minimal_leave_out_07_v1.txt": "5c7b76f86848c5220fe5cbcebc42835fcf330b75355d5347eec2acc70ebe98f7",
    "prompts\\xai\\five_shot_minimal_leave_out_08_v1.txt": "c558b377487c5627c59313d1c221f5f3ea9a94b5ee6bb7c9ebacbfcd248a1557",
    "prompts\\xai\\five_shot_minimal_leave_out_09_v1.txt": "943da00377a4317489d232467dd30571498acacf2e2f4d5fd6ef438eace77a86",
    "prompts\\xai\\five_shot_minimal_leave_out_10_v1.txt": "3a2fe04c4635402ae49238da248fdb4c205cff6d3e2439e73ea54fd7a9adb4a3",
    "prompts\\xai\\five_shot_minimal_leave_out_11_v1.txt": "b4479105f412540119d720c1734adbd4db7b33f83f953e658af420bab7e16d24",
    "prompts\\xai\\five_shot_minimal_leave_out_12_v1.txt": "ba8a4b4c158d81c60c236c6e51371289feb2b3f395836bce7e429f05fbfd0533",
    "prompts\\xai\\five_shot_minimal_leave_out_13_v1.txt": "01f7d83e21a2ed7a9f62f7799a9a4f6085b81f060576328e40f54f96f4a969cd",
    "prompts\\xai\\five_shot_minimal_leave_out_14_v1.txt": "b4e5c12c6e75742c4f57c63dcea4937e9e0f8659910eac259a5f0977821f063a",
    "prompts\\xai\\five_shot_minimal_leave_out_15_v1.txt": "0a84e34551458d4a24048a8f5e852f771f991716fa5017cfe6ee4dad555b1fa6",
    "prompts\\xai\\five_shot_minimal_leave_out_16_v1.txt": "6a4096f7c7fe54b0ca79dbf6a38317014ecfc52025616e1cf448d97e0d3dde2d",
    "prompts\\xai\\five_shot_minimal_leave_out_17_v1.txt": "3abe2a61e63758989207a61a1430043ff3899bc14e13d09e781815014b0aaf02",
    "prompts\\xai\\five_shot_minimal_leave_out_18_v1.txt": "e36d86e82846be8599ce331856e43f4ddcb86b631de86cc90f5fc0897883ca26",
    "prompts\\xai\\five_shot_minimal_leave_out_19_v1.txt": "f324edbed9da52e5fd6cdc488f9c940258719d36e402b995e83998de83f96083",
    "prompts\\xai\\five_shot_minimal_leave_out_20_v1.txt": "c3bebff956c010be7dd3fc84fe8b3c6dfe99eae5f0b8830a512f0cbbb5f8f102",
    "prompts\\xai\\langtag_batch_format_v1.txt": "abfa58da60015816397cd9fe0516263859e8ca326d7a9e3da32d499ecb2edb80",
    "prompts\\xai\\langtag_v1.txt": "1a3392c3e935066b192cdea3113a844639482198a1d27ac627375d57d7a2104a",
    "prompts\\xai\\rationale_batch_format_v1.txt": "88019c3ac1f68b3cde03958be2067e06a673cf35ad04cd2136ec4deb6585006d",
    "prompts\\xai\\rationale_extractive_v1.txt": "f69683aabecdcdc489ec2d34b6681baf2b36964b23ecf473a70db2f38ea20d4b",
    "outputs\\xai\\results\\E6\\dev_rationale_validation__groq__qwen_qwen3.8-27b.json": "9ce1a57488653248d744c55a14acdc895c55be35e94b17b0c91c3455f8b2ec96",
    "outputs\\xai\\results\\E6\\dev_rationale_validation__groq__openai_gpt-oss-20b.json": "eebe6e0511a8f2243549dc8fa96f93a7d8aff596c024a5a8c851ea79fa992e62",
    "outputs\\xai\\annotation\\operator_signoff.csv": "86d8d424948cfb70aafe804fd90d96284eab13de00c06bade4c9c5823afcab69",
    "src\\xai\\__init__.py": "a6633cffdebc85461cd17e107ee9ed07e182532673d9f32fb632b32e3a253c84",
    "src\\xai\\analysis.py": "ac0ab4dd994f2a3e7c24e7231a7d8a6ccb7af2ea8430145b47944e93d53d80e0",
    "src\\xai\\annotations.py": "463577a8fcd0fdff8094dfe60dedc0a6ddbeb26c274ed326495f3c1969742701",
    "src\\xai\\attribution.py": "c20658f724c0a823cc63010726fdb1158770ba8418fdc022f58f88914fdc759a",
    "src\\xai\\cli.py": "e452b8f5608c2b2d345c0f978ba900371196ef51b60c48ddcb43ee9205969b33",
    "src\\xai\\config.py": "c0ccad08867e19cc3144917a591d6fb235b227597ff96db823b9bc804aed4e5d",
    "src\\xai\\counterfactual.py": "a5f7d11e4aafc8131361ace92cd93837d86a716036d11d8acd8dd7591c376826",
    "src\\xai\\dev_workflow.py": "7119469d3e02f269f764b97baf62a9cb870b79c0762ad9011cdb7566f69441c0",
    "src\\xai\\faithfulness.py": "dd48bb5f8260464e3ce55d22afdb903a5abb2b82a1d084f6b74321ff69718136",
    "src\\xai\\gates.py": "233efd8e0f33d80509f7ee555ab1fbc4aa90e46e7d1c48c47550f7ad5df34c25",
    "src\\xai\\instrument.py": "286dbd1b4c2af33ccbcefb2952288cfe107509ccd03217fb5f19ba88148dd6a3",
    "src\\xai\\langtag.py": "a8fd65cd2004adfae5a662341b0ff13919efd61f9fac1b1c19de20cc03a03597",
    "src\\xai\\oracle.py": "ee1a736829b4c863aa7264aa49dd8397d76ee02693df1118a09245aae4e9c53a",
    "src\\xai\\prompt_variants.py": "c4d135a85de6ea6c04eb2de32a2e08fe9509a938caab6dc781bac8f2c541bc7a",
    "src\\xai\\rationale.py": "af86341bbd727b87415c998dd25e594b95c0d73e75476f19b7069cf39bcfdf5c",
    "src\\xai\\report.py": "7e437727b8fc70509d9a374207be537557f40e02cf1c5f20f348ebf9d8d4817e",
    "src\\xai\\results.py": "e5db2471b5bb1ddeb6a16478bab40c98623162831be39ca10a5d6ea669879730",
    "src\\xai\\run_langtag.py": "20685b619d256c79486c9bfcdd96fa05e1706c5f6f3a9bd49b2f4b4e39533456",
    "src\\xai\\sampling.py": "a41059c0de2c009f05ae9c019fe568edad7b2e883bcff609a3837579dac4ce0f",
    "src\\xai\\stats.py": "6fbf522b5d580c62aebc3e47ce1fb4aec1e773d19c65097b0a6046b646479741",
    "src\\xai\\tokenize.py": "ab445cb401769a996c9c37dda9351e0cc4195e805737caac6b3571b621271dea",
    "src\\xai\\validity.py": "d6b70ff90fea24521a9e6de5b95b31af0e1f76c4fd46997093bbbbdc100afbea",
    "src\\xai\\variants.py": "0ec1d8da8524035cd854168cffaabdcda54a6ba37b4b509032c8343997158c7d",
    "XAI Experiment Plan Behavioural Explainability of LLM Sentiment Classification on Code-Mixed Bengali-English Text.md": "85bd55f0a95a8f3d270636bac078e6c68357566e95837f68cbaaece2b8deed61"
  },
  "hypotheses": {
    "P1": "Coalition top-3 comprehensiveness exceeds 3-random-word comprehensiveness; paired bootstrap CI excludes 0.",
    "P2": "Self-rationale evidence comprehensiveness exceeds size-matched random evidence; paired bootstrap CI excludes 0.",
    "P3": "For baseline-Mixed rows with a strict marker, deleting either clause moves away from Mixed at least 0.10 above the noise floor.",
    "P4": "On single-polarity rows with one lexicon hit, antonym swapping flips to the opposite polarity at least 0.10 above noise.",
    "P5": "Each of eight prompt ablations changes correctness; paired McNemar tests, Holm-corrected within family."
  },
  "dev_gate": {
    "G1": {
      "groq/qwen/qwen3.8-27b": {
        "agreement_A_A2": {
          "n": 585,
          "agreement": 1.0,
          "cohen_kappa": 1.0
        },
        "agreement_A_B": {
          "n": 585,
          "agreement": 0.8854700854700854,
          "cohen_kappa": 0.8345853555602447
        },
        "agreement_A_C": {
          "n": 585,
          "agreement": 0.764102564102564,
          "cohen_kappa": 0.6584230679726671
        },
        "epsilon": 0.0,
        "noisy": false
      },
      "groq/openai/gpt-oss-20b": {
        "agreement_A_A2": {
          "n": 585,
          "agreement": 0.9863247863247864,
          "cohen_kappa": 0.979606776824932
        },
        "agreement_A_B": {
          "n": 585,
          "agreement": 0.8170940170940171,
          "cohen_kappa": 0.7294908749897362
        },
        "agreement_A_C": {
          "n": 585,
          "agreement": 0.7316239316239316,
          "cohen_kappa": 0.595921599683231
        },
        "epsilon": 0.013675213675213627,
        "noisy": false
      }
    },
    "G2": {
      "lr_median_spearman": 0.6833637196362471,
      "lr_top1_agreement": 0.676056338028169,
      "planted_cue_top1_rate": 0.865979381443299,
      "coalition_budget": 96,
      "pipeline_limit": "occlusion_only",
      "planted_cue_budget_tested": 96
    }
  },
  "rationale_prompt_validation": {
    "groq/qwen/qwen3.8-27b": {
      "parse_rate": 1.0,
      "verbatim_match_rate": 0.961220597584234,
      "requested": 580,
      "parsed": 580,
      "words": 1573,
      "matched_words": 1512
    },
    "groq/openai/gpt-oss-20b": {
      "parse_rate": 1.0,
      "verbatim_match_rate": 0.9081920903954802,
      "requested": 576,
      "parsed": 576,
      "words": 708,
      "matched_words": 643
    }
  }
}
```
