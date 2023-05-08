
# Soilitix

## Optimize your crop and plant growth with Soilitix - the web application for tracking soil health metrics like temperature, moisture, and humidity.

<br>

![soilitix](./Images/soilitix.png)

<br>

Soilitix is a web application designed for monitoring soil health. It allows farmers and gardeners to track important soil metrics such as temperature, moisture, and humidity. The application provides an easy-to-use interface that enables users to visualize and analyze their soil data, helping them make informed decisions about their crops and plants.

Using Soilitix is simple and straightforward. Users can connect their sensors to the application, and the data is automatically collected and stored in a Google Sheet. The data can then be visualized using Plotly, a powerful data visualization library that enables users to create interactive graphs and charts.

One of the key features of Soilitix is the ability to track soil data over time. Users can select a date range and view data for that specific period, allowing them to identify trends and patterns in their soil health. The application also provides a slider that allows users to adjust the number of data points displayed, giving them more control over their data analysis.

In addition to tracking soil health metrics, Soilitix also allows users to set alerts for specific conditions. For example, users can set an alert to notify them when the soil temperature drops below a certain threshold. This feature helps users stay on top of their soil health and take action before any problems arise.

Overall, Soilitix is a robust tool for anyone who wants to monitor their soil health and optimize their crop and plant growth. Its user-friendly interface, robust data analysis capabilities, and customizable alerts make it an essential tool for farmers, gardeners, and anyone else who cares about their soil health.

<hr>

## ⭐ Challenges Faced:

Building a soil health monitoring web application like Soilitix can be a complex process, involving several challenges that must be addressed to ensure a successful outcome. Some of the challenges that may be faced in building Soilitix could include:

* `Data collection:` One of the main challenges in building Soilitix would be collecting accurate and reliable data from sensors. Sensors can sometimes provide inaccurate readings, or the data may be affected by external factors such as weather conditions or interference from other devices.

* `Data processing and analysis:` Once the data has been collected, it must be processed and analyzed to identify patterns and trends. This can be a time-consuming process, and it requires a robust data analysis framework to ensure accurate results.

* `Data visualization:` After processing and analysis, the data must be presented in a clear and easy-to-understand format. This requires the use of data visualization tools, such as charts and graphs, that can effectively convey complex information in a simple and intuitive way.

* `User interface design:` Soilitix must have a user-friendly interface that makes it easy for users to access and understand their data. This requires careful consideration of design principles, such as usability, accessibility, and visual aesthetics.

* `Security and privacy:` Soilitix will be handling sensitive data about soil health and user information. Ensuring the security and privacy of this data is critical to maintaining user trust and compliance with data protection regulations.

Addressing these challenges requires a multidisciplinary approach that combines expertise in software development, data analysis, user experience design, and security. It also requires a willingness to adapt and iterate based on user feedback and changing technological landscapes.



<hr>

## ⭐ Development References:
1. https://docs.fast.ai/
2. https://dirk-kalmbach.medium.com/datablock-and-dataloaders-in-fastai-d5aa7ae560e5
3. https://benjaminwarner.dev/2021/10/01/inference-with-fastai
4. https://youtu.be/e8yq1saR7Pk


<hr>

## ⭐ Streamlit Deployment Configurations:
```
[theme]
primaryColor = "#E694FF"
backgroundColor = "#00172B"
secondaryBackgroundColor = "#0083B8"
textColor = "#DCDCDC"
font = "sans serif"

[browser]
gatherUsageStats = false
```

<hr>


## ⭐ Deployment References:
1. https://30days.streamlit.app/
2. https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app
3. https://streamlit-cloud-example-apps-streamlit-app-sw3u0r.streamlit.app/?hsCtaTracking=28f10086-a3a5-4ea8-9403-f3d52bf26184|22470002-acb1-4d93-8286-00ee4f8a46fb
4. https://docs.streamlit.io/library/advanced-features/configuration

<hr>

## ⭐ To frame the credentials in the google-creds.json file, you need to follow these steps:

1. Go to the Google Cloud Console.
2. Create a new project or select an existing project.
3. Enable the Google Sheets API for your project:
    1. Go to the APIs & Services > Dashboard page.
    2. Click on the "+ ENABLE APIS AND SERVICES" button.
    3. Search for "Google Sheets API" and select it.
    4. Click on the "Enable" button.
4. Create a service account:
    1. Go to the APIs & Services > Credentials page.
    2. Click on the "+ CREATE CREDENTIALS" button.
    3. Select "Service account key".
    4. Select "New service account".
    5. Give the service account a name and select the "Project" role.
        6. Click on the "Create" button.
    7. Download the JSON file that contains the service account key.
5. Share the Google Sheet with the service account email address:
    1. Open the Google Sheet.
    2. Click on the "Share" button.
    3. Enter the service account email address in the "People" field.
    4. Select the "Editor" or "Viewer" role.
    5. Click on the "Send" button.
6. Copy the contents of the downloaded JSON file into a new file named google-creds.json in your project directory.