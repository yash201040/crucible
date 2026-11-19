# agent-sdk-input-and-output/agent-sdk-user-input

* [Handle AskUserQuestion clarifying questions](askuserquestion-clarifying-questions.md) - Detect AskUserQuestion in canUseTool, parse the questions array and return an answers map keyed by question text. **[high]**
* [AskUserQuestion option previews (TypeScript)](askuserquestion-option-previews.md) - toolConfig.askUserQuestion.previewFormat adds a markdown or html preview field to each option.
* [canUseTool callback for approvals](cantooluse-callback.md) - A canUseTool callback pauses execution when a tool needs approval or Claude asks a question, and can stay pending indefinitely. **[high]**
* [Other ways to get user input](other-ways-to-get-user-input.md) - Streaming input and custom tools as alternatives to canUseTool and AskUserQuestion.
* [Tool approval arguments and response options](tool-approval-request-and-responses.md) - Arguments passed to canUseTool, common tool input fields, allow/deny return shapes, and the ways to respond including remembered rules. **[high]**
