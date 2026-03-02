## Data Ingestion

**PeakTDM FileFocus** uses [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/2.11.1/index.html) and [ExD API-Plugins](https://peak-solution.github.io/data_management_learning_path/exd_api/overview.html) for data ingestion.

## Apache Airflow

Apache Airflow® is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows. 

**PeakTDM FileFocus** uses Airflow DAGs to manage and control the data ingestion pipeline. 

| Airflow DAG                     | Description |
| -----------                     | ----------- |
| FileFocus Crawler               | Inspect the index folder defined in the [.env configuration file](envconfig.md) for new files |
| FileFocus Import File           | Import a new file into the data index |
| FileFocus Statistics Calculator | Calculate channel KPIs such as minimun, maximum, ... |
| FileFocus Remove Import         | Remove no longer existing files from the data index |
| Check unknown units             | Create default engineering units |

## ExD DataPlugins

ExD API-Plugins are used to extract descriptive data (meta data) and channel data (bulk data) from a measurement file. The following ExD API-Plugins are installed by default:

| name           | extension      | link |
| -------------- | -----------    | ---- |
| ASAM ODS mdf4  | \*.mf4         | [asam_ods_exd_api_mdf4](https://github.com/peak-solution/asam_ods_exd_api_mdf4?tab=readme-ov-file#readme) |
| Dewesoft DxD   | \*.d7d, \*.dxd | [asam_ods_exd_api_dewesoft](https://github.com/peak-solution/asam_ods_exd_api_dewesoft?tab=readme-ov-file#readme) |
| Excel example  | \*.xlsx        | [asam_ods_exd_api_excel](https://github.com/peak-solution/asam_ods_exd_api_xlsx?tab=readme-ov-file#readme) |
| parquet       | \*.parquet      | [asam_ods_exd_api_parquet](https://github.com/totonga/asam_ods_exd_api_parquet?tab=readme-ov-file#readme) |
| NI tdms       | \*.tdms         | [asam_ods_exd_api_nptdms](https://github.com/totonga/asam_ods_exd_api_nptdms?tab=readme-ov-file#readme) |
| IMC Termite   | \*.dat;\*.raw   | [asam_ods_exd_api_IMCtermite](https://github.com/totonga/asam_ods_exd_api_IMCtermite?tab=readme-ov-file#readme) |
| CSV           | \*.csv          | [asam_ods_exd_api_pandascsv](https://github.com/totonga/asam_ods_exd_api_pandascsv#readme) |


ExD API-Plugins are defined by the [ASAM ODS standard](https://www.asam.net/standards/detail/ods/wiki/).