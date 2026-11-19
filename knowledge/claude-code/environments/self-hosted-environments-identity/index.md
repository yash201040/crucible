# environments/self-hosted-environments-identity

* [Session token claims and act chain](token-claims-reference.md) - Claims in the self-hosted session JWT, including ccr:* claims, flat duplicates and the RFC 8693 act delegation chain.
* [Verify the session access token](verify-session-token.md) - Every self-hosted session gets an ES256 JWT in CLAUDE_CODE_SESSION_ACCESS_TOKEN; services verify it against Anthropic's JWKS. **[high]**
