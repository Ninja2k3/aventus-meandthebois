from bs import bill_info
urls=['https://prsindia.org/billtrack/the-prohibition-of-child-marriage-amendment-bill-2021','https://prsindia.org/billtrack/the-pesticide-management-bill-2020','https://prsindia.org/billtrack/the-jan-vishwas-amendment-of-provisions-bill-2022','https://prsindia.org/billtrack/the-constitution-scheduled-tribes-order-third-amendment-bill-2022','https://prsindia.org/billtrack/the-forest-conservation-amendment-bill-2023']
mega_data=[]
for url in urls:
    bill=bill_info(url)
    mega_data.append(bill.scrape())
for i in mega_data:
    print(i)
    print("\n\n\n")
    