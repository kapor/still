----
-- phpLiteAdmin database dump (https://www.phpliteadmin.org/)
-- phpLiteAdmin version: 1.9.9-dev
-- Exported: 8:22pm on February 8, 2025 (UTC)
-- database file: ../aaa/db.sqlite3
----
BEGIN TRANSACTION;

----
-- Table structure for auth_user
----
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);

----
-- Data dump for auth_user, a total of 5 rows
----
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES ('1','pbkdf2_sha256$600000$hVKh7L8cFFrUcYdNwOgEBo$TUebRplahBsZoWRNH25QE/PldsFVrAJ/b7VZo3D4qMM=','2025-02-08 20:20:07.324366','1','taco','taco','aaronkapor@gmail.com','1','1','2025-01-27 02:45:22','taco');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES ('2','pbkdf2_sha256$600000$qLAXBC9xTifThi61q6KK7e$bu4jv5vArIBK9HfyKnFGwqvG8PGG5/AZ3BgixU8JhWI=','2025-02-04 05:05:23','1','aaa','kapor','aaronkapor@gmail.com','1','1','2025-01-27 12:46:41','aaa');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES ('3','pbkdf2_sha256$600000$FqzOWqoPhn25GBIbotkCvh$8K1RNHOWYxZuRW1hy6Kt7BVXBX0tLcTtlgsYBdttF0k=','2025-01-27 12:50:00','1','burrito','burrito','burrito@burrito.com','1','1','2025-01-27 12:48:16','burrito');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES ('4','pbkdf2_sha256$600000$iaI3DdHmDpHbcXRk3O59ta$HWmtOY8UAUoEn/jspdPBUje8bq6YGgaWJWvJOye5gxs=','2025-01-30 23:49:31.125085','0','nothing_fancy','','aaronkapor@gmail.com','0','1','2025-01-30 23:49:24.408819','');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES ('5','pbkdf2_sha256$600000$0wHelbJqBJoVkjpvk1XdCV$3+HyxHud0MXvk29X7AGs+Wzv3zmK9PrBRLzmh4mKPdw=','2025-02-08 15:25:24.330758','0','dangerous','','dangerous@dangerous.com','0','1','2025-02-08 15:25:18.369725','');

----
-- structure for index sqlite_autoindex_auth_user_1 on table auth_user
----
;
COMMIT;
