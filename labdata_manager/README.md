# Django Labdata-manager

The purpose of this project is to develop a web application that enables a laboratory company to efficiently and accurately manage their testing operations. The web app will store and manipulate laboratory data, including test results and supply inventory, and provide a platform for customers to place orders and receive results via email. The web app will also enable employees to manage orders, add new supplies and tests to the database, and generate reports.

There will be restful apis (mostly customer facing interfaces, eg order and account creation), and graphql (for employee facing interfaces, mostly for data processing)

Because the models have strong relationships with each other, we will use sql. Initially mysql and will upgrade to postgres in the future