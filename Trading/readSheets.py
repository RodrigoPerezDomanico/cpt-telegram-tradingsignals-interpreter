from auth0logger import logg_in

SPREADSHEET_ID='1drl3Azngj8AYp7pvtEGiw4iSZZL1ebMbDi3Tzpx4Nas'
RANGE_NAME="Hoja 1!A1:C"
if __name__ == '__main__':
    values=logg_in(SPREADSHEET_ID, RANGE_NAME,'read')
    print(values,len(values))

    # batch_get_values("13kVXlWzeprpben1PAnR-qsbiWLKrM4cS4F3fdKJcrrA", "A1:A3")