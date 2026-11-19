# agent-sdk-input-and-output/agent-sdk-structured-outputs

* [Output format options, JSON Schema support, Zod and Pydantic](schema-format-and-zod-pydantic.md) - outputFormat fields, the draft-07 requirement, supported schema features, format keyword handling, and generating schemas from Zod or Pydantic.
* [Structured output errors and retries](structured-output-error-handling.md) - error_max_structured_output_retries, success-without-output cases, model-fallback retraction and tips for avoiding failures. **[high]**
* [Structured outputs quick start](structured-outputs-quick-start.md) - Pass a JSON Schema via outputFormat (TS) or output_format (Python) and read validated JSON from structured_output on the result message. **[high]**
* [The StructuredOutput tool call](structuredoutput-tool-call.md) - Claude Code adds a StructuredOutput tool to sessions with an output format; the agent calls it to return its answer, possibly several times.
