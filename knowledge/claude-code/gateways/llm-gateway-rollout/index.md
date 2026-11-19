# gateways/llm-gateway-rollout

* [Distribute gateway configuration through managed settings](distribute-gateway-configuration.md) - Table of variables to push (base URL, credential, hint headers, discovery, beta disabling, fast mode, model pins) and managed-settings delivery caveats. **[high]**
* [Gateway product requirements and rollout checkpoints](gateway-requirements.md) - What a gateway must do (format, streaming, routing, header pass-through, unmodified errors, WAF exemption) and the five rollout steps with checkpoints. **[high]**
* [HIPAA configuration behind a gateway](hipaa-behind-gateway.md) - Sessions through a gateway are not eligible for the HIPAA configuration; managed keys can restrict features but do not replicate it.
* [Maintain the gateway and plan Claude Code upgrades](maintain-and-pin-gateway.md) - Keep a gateway current with new betas, models and credential rotation, and pin Claude Code versions so version-dependent defaults stay constant. **[high]**
