README OUTDATED

---

# Distance calculator
WEB application for path length calculation based on given points coordinates (using *GeoDistance* REST API)

The user can provide a list of points. After submitting, total distance of the path and the calculation time are displayed.

---  

## App usage
The user can select **number of points** in the path between 2 and 50. After submission, given number of point inputs are generated.  

**Latitude** inputs accept values between -90 and 90. **Longitude** inputs accept values between -180 and 180. Both latitude and longitude accept values up to 7 decimal places which gives an accuracy of 1cm. All input fields are validated and the user gets proper feedback if any value is invalid.  

**Request_id** value is optional and is automatically set to "request_xyz" (where xyz is current timestamp) when no value given. Submitting given points coordinates starts the calculations. After the calculations are finished, distance and time are displayed. Request_id and timestamps of start and end of calculations are stored in database. If user provides request_id already existing in database, the record is overrided.

---

## Admin panel
To access admin panel and database, go to "*/admin*" and use superuser account with the following credentials:  
>*Username:* **admin**  
*Password:* **adminpassword**

---

## Calculating path distance
After submitting provided data, user is redirected to url "***/requestId/pointsString/***" which contains **request_id** value and all **points coordinates** serialized to proper string. GET method handles these values.  

For each pair of points there's request sent to *GeoDistance* REST API. In case of *504 Gateway Timeout* error, request is resent up to 5 times. Sending requests is asynchronous for faster results. After all responses are gathered, distances are added up and returned as total distance. In case of calculation error, an alert is displayed. 

### GeoDistance request example:  
*http://146.59.46.40:60080/route?origin=50.0,18.1&destination=50.2,18.3*  
With authentication credentials:  
*('Cristoforo', 'Colombo')*
