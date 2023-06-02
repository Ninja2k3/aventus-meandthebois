from bs import bill_info
text='https://prsindia.org/billtrack/the-tamil-nadu-legislative-council-repeal-bill-2012'
bill=bill_info(text)
data=bill.scrape()
print(data+'\n\n')
bill.show()