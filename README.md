Open Jira Task
================

The "Open Jira Task" plugin extracts task IDs from Git branch name and provides a convenient way to open those tasks directly in a web browser

`TASK-7345 some cool feature` => `...atlassian.net/browse/TASK-7345`

## Key Binding
```json
{
	"keys": ["shift+f6"],
	"command": "open_jira_task"
}
```

## Commands

```json
{
	"caption": "Open Jira Task",
	"command": "open_jira_task"
}
```

## Settings

Set in `.sublime-project file`

```json
{
	"folders":
	[
		{
			"path": "PROJECT_PATH"
		}
	],
	"settings":
	{
		"jira_url": "https://organisation.atlassian.net",
		"jira_task_regexp": "TASK-\\d+"
	}
}
```
---