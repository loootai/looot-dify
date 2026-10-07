# Privacy policy

This plugin connects Dify to looot (https://looot.ai). Full policy: https://looot.ai/privacy. Terms: https://looot.ai/terms. Contact: hello@looot.ai.

## What the plugin sends

Every request goes over HTTPS to https://api.looot.ai and nowhere else. The plugin sends:

- Your looot agent token, in the Authorization header. Dify stores it as an encrypted credential. The plugin never logs it, writes it to disk or includes it in error messages.
- Search text, endpoint ids, run ids and the JSON input of a run, exactly as your workflow or agent passes them. A run input can contain personal data you chose to look up, such as a person's name, a company domain or an email address.

The plugin sends no telemetry, analytics or usage data of its own. It keeps no state between calls.

## How looot uses the data

looot forwards a run's input to the data provider that serves the endpoint you called (for example an email finder or a search API) so the provider can answer. It records the run, its cost and its result against your looot account so you can read it back with Get run and see it in your ledger. See https://looot.ai/privacy for retention periods and for how to request deletion.

## Data the plugin does not collect

No Dify user data, workspace data, conversation history or files are read or sent. Only the parameters of the tool call are sent.

## Contact

Privacy questions: hello@looot.ai
