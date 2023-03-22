from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


plugin_buttons = [
    PluginMenuButton(
        link='plugins:netbox_application_list_plugin:applicationlist_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_application_list_plugin:applicationlist_list',
        link_text='Application List',
        buttons=plugin_buttons
    ),
)
