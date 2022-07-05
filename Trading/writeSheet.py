from auth0logger import logg_in

SPREADSHEET_ID='1drl3Azngj8AYp7pvtEGiw4iSZZL1ebMbDi3Tzpx4Nas'
RANGE_NAME="Hoja 1!A1:C"
# VALUES=
if __name__ == '__main__':
    values=logg_in(SPREADSHEET_ID, RANGE_NAME,'write')
    # print(values,len(values))