import csv


def create_csv(file_path, asset_name_custom1):
    headers = [
        "Domain", "IPAddress", "OScode", "SP", "Description", "Assettype", "AssetName", "FQDN", "Mac",
        "Memory (MB)", "NrProcessors", "Processor", "State", "PurchaseDate", "Warrantydate",
        "LastPatched", "LastFullbackup", "LastFullimage", "OrderNumber", "Comments", "Location",
        "Building", "Department", "Branchoffice", "BarCode", "Manufacturer", "Contact", "Model",
        "Serialnumber", "Scanserver", "Chrome OS Device ID", "System SKU", "Custom1", "Custom2",
        "Custom3", "Custom4", "Custom5", "Custom6", "Custom7", "Custom8", "Custom9", "Custom10",
        "Custom11", "Custom12", "Custom13", "Custom14", "Custom15", "Custom16", "Custom17",
        "Custom18", "Custom19", "Custom20"
    ]

    row = [
        "TRWIN", "", "10.0.10240", "", "", "Windows", asset_name_custom1, "", "",
        "", "", "", "Active", "", "",
        "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "",
        "", asset_name_custom1, "", "", "",
        "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", ""
    ]

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(row)


def main():
    asset_name_custom1 = input("Enter AssetName: ")
    create_csv('test1.csv', asset_name_custom1)
    print("CSV file 'test1.csv' created successfully.")


if __name__ == "__main__":
    main()
