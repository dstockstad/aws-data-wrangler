"""Amazon Glue Catalog Module."""

from awswrangler.catalog._add import add_column, add_csv_partitions, add_json_partitions, add_parquet_partitions  # noqa
from awswrangler.catalog._create import (  # noqa
    _create_csv_table,
    _create_json_table,
    _create_parquet_table,
    create_csv_table,
    create_database,
    create_json_table,
    create_parquet_table,
    overwrite_table_parameters,
    upsert_table_parameters,
)
from awswrangler.catalog._delete import (  # noqa
    delete_all_partitions,
    delete_column,
    delete_database,
    delete_partitions,
    delete_table_if_exists,
)
from awswrangler.catalog._get import (  # noqa
    _get_table_input,
    databases,
    get_columns_comments,
    get_connection,
    get_csv_partitions,
    get_databases,
    get_parquet_partitions,
    get_partitions,
    get_table_description,
    get_table_location,
    get_table_number_of_versions,
    get_table_parameters,
    get_table_types,
    get_table_versions,
    get_tables,
    search_tables,
    table,
    tables,
)
from awswrangler.catalog._utils import (  # noqa
    does_table_exist,
    drop_duplicated_columns,
    extract_athena_types,
    sanitize_column_name,
    sanitize_dataframe_columns_names,
    sanitize_table_name,
)

__all__ = [
    "add_column",
    "add_csv_partitions",
    "add_json_partitions",
    "add_parquet_partitions",
    "does_table_exist",
    "delete_column",
    "drop_duplicated_columns",
    "extract_athena_types",
    "sanitize_column_name",
    "sanitize_dataframe_columns_names",
    "sanitize_table_name",
    "_create_csv_table",
    "_create_parquet_table",
    "_create_json_table",
    "create_csv_table",
    "create_database",
    "create_parquet_table",
    "create_json_table",
    "overwrite_table_parameters",
    "upsert_table_parameters",
    "_get_table_input",
    "databases",
    "get_columns_comments",
    "get_connection",
    "get_csv_partitions",
    "get_databases",
    "get_parquet_partitions",
    "get_partitions",
    "get_table_description",
    "get_table_location",
    "get_table_number_of_versions",
    "get_table_parameters",
    "get_table_types",
    "get_table_versions",
    "get_tables",
    "search_tables",
    "table",
    "tables",
    "delete_database",
    "delete_table_if_exists",
    "delete_partitions",
    "delete_all_partitions",
]
