
import import_declare_test

from splunktaucclib.rest_handler.endpoint import (
    field,
    validator,
    RestModel,
    DataInputModel,
)
from splunktaucclib.rest_handler import admin_external, util
from splunktaucclib.rest_handler.admin_external import AdminExternalHandler
import logging

util.remove_http_proxy_env_vars()


fields = [
    field.RestField(
        'input_one_checkbox',
        required=False,
        encrypted=False,
        default=True,
        validator=None
    ), 
    field.RestField(
        'input_one_radio',
        required=False,
        encrypted=False,
        default='yes',
        validator=None
    ), 
    field.RestField(
        'singleSelectTest',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'multipleSelectTest',
        required=False,
        encrypted=False,
        default='a|b',
        validator=None
    ), 
    field.RestField(
        'interval',
        required=True,
        encrypted=False,
        default=None,
        validator=validator.Pattern(
            regex=r"""^\-[1-9]\d*$|^\d*$""", 
        )
    ), 
    field.RestField(
        'index',
        required=True,
        encrypted=False,
        default='default',
        validator=validator.String(
            max_len=80, 
            min_len=1, 
        )
    ), 
    field.RestField(
        'account',
        required=True,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'object',
        required=True,
        encrypted=False,
        default=None,
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'object_fields',
        required=True,
        encrypted=False,
        default=None,
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'order_by',
        required=True,
        encrypted=False,
        default='LastModifiedDate',
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'use_existing_checkpoint',
        required=False,
        encrypted=False,
        default='yes',
        validator=None
    ), 
    field.RestField(
        'start_date',
        required=False,
        encrypted=False,
        default=None,
        validator=validator.Pattern(
            regex=r"""^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}z)?$""", 
        )
    ), 
    field.RestField(
        'limit',
        required=False,
        encrypted=False,
        default='1000',
        validator=validator.String(
            max_len=8192, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'example_help_link',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 

    field.RestField(
        'disabled',
        required=False,
        validator=None
    )

]
model = RestModel(fields, name=None)



endpoint = DataInputModel(
    'example_input_one',
    model,
)


if __name__ == '__main__':
    logging.getLogger().addHandler(logging.NullHandler())
    admin_external.handle(
        endpoint,
        handler=AdminExternalHandler,
    )
