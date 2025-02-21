`Configuration` tab can have multiple subtabs, for example, a tab for account configuration (Use to configure the account by adding account credentials), proxy configuration and logging level configuration.

### Configuration Properties

| Property                                                         | Type   | Description                                          |
| ---------------------------------------------------------------- | ------ | ---------------------------------------------------- |
| title<span class="required-asterisk">*</span>                    | string | -                                                    |
| description                                                      | string | To provide a brief summary of an configuration page. |
| [tabs](#tabs-properties)<span class="required-asterisk">*</span> | array  | To specify a list of tab.                            |


### Tabs properties

| Property                                       | Type   | Description                                                                                                                                                                                        |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name<span class="required-asterisk">*</span>   | string | To define the particular tab name.                                                                                                                                                                 |
| title<span class="required-asterisk">*</span>  | string | To show the title of the tab.                                                                                                                                                                      |
| [entity](../entity)<span class="required-asterisk">*</span> | array  | A list of fields and their properties.                                                                                                                                                             |
| [table](../table)                                          | object | To display accounts stanza in table                                                                                                                                                                |
| style                                          | string | By specifying this property in the global config file, the forms can either be opened as a new page or in a dialog. <br>Supported values are "page" or "dialog". <br> Default value is **dialog**. |
| options                                        | object | This property allows you to enable the [saveValidator](../advanced/save_validator) feature.                                                                                                        |
| hook                                           | object | It is used to add custom behaviour to forms. Visit the [Custom Hook](../custom_ui_extensions/custom_hook) page to learn more.                                                                      |
| conf                                           | string | TBD                                                                                                                                                                                                |
| restHandlerName                                | string | TBD                                                                                                                                                                                                |
| restHandlerModule                              | string | TBD                                                                                                                                                                                                |
| restHandlerClass                               | string | TBD                                                                                                                                                                                                |
| customTab                                      | Object | This property allows you to enable the [custom tab](../custom_ui_extensions/custom_tab) feature.                                                                                                   |

### Usage

```
"configuration": {
    "title": "Configuration",
    "description": "Set up your add-on",
    "tabs": [
        {
            "name": "account",
            "title": "Account"
            "table": {},
            "entity": []
        },
        {
            "name": "proxy",
            "title": "Proxy"
            "entity": [],
            "options": {
                "saveValidator": ""
            },
        }
    ]
}
```

### Output

This is how table looks in the UI:

![image](images/configuration/configuration_with_table_output.png)

This is how form looks in the UI:

![image](images/configuration/configuration_without_table_output.png)
