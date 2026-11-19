# deployment/amazon-bedrock

* [Bedrock AWS credentials and refresh](bedrock-aws-credentials.md) - Credential methods, in-memory caching, timeouts and the awsAuthRefresh and awsCredentialExport settings for Claude Code on Bedrock. **[high]**
* [Amazon Bedrock Mantle endpoint](bedrock-mantle-endpoint.md) - Mantle serves Claude through the native Anthropic API shape on Bedrock; how to enable it, pick models, combine with Invoke and route via a gateway.
* [Bedrock model pinning and startup checks](bedrock-model-pinning-checks.md) - Pin model versions on Bedrock, map versions to inference profile ARNs, and how startup checks, fallbacks and allowlists behave. **[high]**
* [Bedrock prefixes, IAM, 1M context, tiers, guardrails](bedrock-prefixes-iam-context.md) - Cross-region inference profile prefixes, required IAM actions, 1M context behavior, service tiers and Guardrails headers on Bedrock.
* [Amazon Bedrock setup, wizard and region](bedrock-setup-and-region.md) - Enable Claude Code on Amazon Bedrock with the /setup-bedrock wizard or environment variables, and how the AWS region is resolved. **[high]**
* [Bedrock troubleshooting](bedrock-troubleshooting.md) - Fixes for SSO auth loops, TLS-inspecting proxy certificate errors, region and throughput errors, gateway streaming content-type errors and zero /context counts.
