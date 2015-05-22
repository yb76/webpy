import web
import json

db = web.database( dbn="mysql", db="webgomo", host="gm-cabs-db-master-production.cbavz7bmtquu.ap-southeast-2.rds.amazonaws.com", user="iris", passwd="th1nkr1s")
dbgm = web.database( dbn="mysql", db="gmcabs", host="gm-cabs-db-master-production.cbavz7bmtquu.ap-southeast-2.rds.amazonaws.com", user="iris", passwd="th1nkr1s")


def get_driver(id):
    strsql = "Select profile.FirstName,profile.Lastname,profile.MobileNumber,user.Email,concat(address.AddressLine1,address.AddressLine2) as Address,address.Suburb,address.PostCode,ref_state.Description as State,date_format(profile.DateOfBirth,'%Y%m%d') as DateOfBirth,driver.DriversLicence,driver.owner HireCar from driver left join profile on driver.profileid = profile.id left join user on profile.userid = user.id left join address on profile.addressid = address.id left join ref_state on ref_state.id = address.stateid where driver.driversnumber = $id"
    #strsql = "Select profile.FirstName,profile.Lastname,profile.MobileNumber,user.Email,address.AddressLine1 as Address,address.Suburb,address.PostCode,ref_state.Description as State,date(profile.DateOfBirth) as DateOfBirth,driver.DriversLicence,0 as LicenseExpiry,driver.owner HireCar from driver left join profile on driver.profileid = profile.id left join user on profile.userid = user.id left join address on profile.addressid = address.id left join ref_state on ref_state.id = address.stateid where driver.driversnumber = $id"
    #strsql = "Select profile.FirstName from driver left join profile on driver.profileid = profile.id where driver.driversnumber = $id"
    print strsql 
    result = dbgm.query(strsql , vars=locals())
    if result:
        str=json.dumps(result[0])
        print str
        return str
    else:
        return result
