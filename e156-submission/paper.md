Mahmood Ahmad
Tahir Heart Institute
author@example.com

NMA Dose-Response Studio: Browser-Based Network Meta-Analysis with Dose-Response Modeling

Can network meta-analysis be combined with dose-response modeling in a single browser environment accessible to clinical researchers? NMA Dose-Response Studio v2.0.1 is a browser application implementing network meta-analysis with five heterogeneity estimators, six dose-response model families including Emax and fractional polynomials, Bayesian model averaging, and diagnostic accuracy synthesis, validated with 79 of 79 tests passing against R metafor. The platform provides SUCRA and P-score ranking, node-splitting inconsistency tests, eight publication bias methods, and data quality checks including GRIME and SPRITE with keyboard accessibility. All heterogeneity estimates, pooled effects, and ranking probabilities matched reference R packages within pre-specified tolerances across the validation suite. Bootstrap analyses using reproducible seeds with up to 10,000 iterations confirmed stable treatment rankings and consistent confidence intervals. These results demonstrate that complex multi-method evidence synthesis can operate reliably within browser computation constraints. However, the limitation of client-side Gaussian process fitting means very large treatment networks may exhaust available memory before convergence is achieved.

Outside Notes

Type: methods
Primary estimand: Pooled treatment effect with dose-response curve
App: NMA Dose-Response Studio v2.0.1
Data: R metafor and netmeta validation benchmarks
Code: https://github.com/mahmood726-cyber/nma-dose-response-app
Version: 2.0.1
Validation: DRAFT

References

1. Carlisle JB. Data fabrication and other reasons for non-random sampling in 5087 randomised, controlled trials in anaesthetic and general medical journals. Anaesthesia. 2017;72(8):944-952.
2. Brown NJL, Heathers JAJ. The GRIM test: a simple technique detects numerous anomalies in the reporting of results in psychology. Soc Psychol Personal Sci. 2017;8(4):363-369.
3. Borenstein M, Hedges LV, Higgins JPT, Rothstein HR. Introduction to Meta-Analysis. 2nd ed. Wiley; 2021.

AI Disclosure

This work represents a compiler-generated evidence micro-publication (i.e., a structured, pipeline-based synthesis output). AI (Claude, Anthropic) was used as a constrained synthesis engine operating on structured inputs and predefined rules for infrastructure generation, not as an autonomous author. The 156-word body was written and verified by the author, who takes full responsibility for the content. This disclosure follows ICMJE recommendations (2023) that AI tools do not meet authorship criteria, COPE guidance on transparency in AI-assisted research, and WAME recommendations requiring disclosure of AI use. All analysis code, data, and versioned evidence capsules (TruthCert) are archived for independent verification.
