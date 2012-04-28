** DONE 
   CLOSED: [2011-01-05 Wed 09:05]
   - how to create user and database and grant all privilges (detail
     at manul 5.5.2
     CREATE USER 'monty'@'%' IDENTIFIED BY 'some_pass';
     GRANT ALL PRIVILEGES ON *.* TO 'monty'@'%'
     
SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('newpass');
REVOKE INSERT ON *.* FROM 'jeffrey'@'localhost';
