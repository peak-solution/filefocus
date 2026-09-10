"""Test reading data from a custom CSV file."""

if __name__ == "__main__":
    import pathlib

    from external_file_data import ExternalFileData

    example_file_path = (
        pathlib.Path(__file__).parent.parent / "datafolder" / "custom_csv" / "data.dat"
    )
    assert example_file_path.exists()

    exd_file = ExternalFileData(str(example_file_path), {})

    print(exd_file.data())
    print("column_units():", exd_file.column_units())
    print("not_my_file():", exd_file.not_my_file())
