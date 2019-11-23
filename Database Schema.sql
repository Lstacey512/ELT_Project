-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/v9lXvw
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Artwork" (
    "Object_id" INT   NOT NULL,
    "Object_type" VARCHAR   NOT NULL,
    "Title" VARCHAR   NOT NULL,
    "Date_started" VARCHAR   NOT NULL,
    "Date_finished" VARCHAR   NOT NULL,
    "Medium" VARCHAR   NOT NULL,
    "Classification" VARCHAR   NOT NULL,
    "Met_link" VARCHAR   NOT NULL,
    "Artist_id" INT   NOT NULL,
    "Dept_id" INT   NOT NULL
);

CREATE TABLE "Department" (
    "Dept_id" INT   NOT NULL,
    "Dept_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Department" PRIMARY KEY (
        "Dept_id"
     )
);

CREATE TABLE "Artist" (
    "Surname" VARCHAR   NOT NULL,
    "First_name" VARCHAR   NOT NULL,
    "Full_name" VARCHAR   NOT NULL,
    "Birth_date" VARCHAR   NOT NULL,
    "Death_date" VARCHAR   NOT NULL,
    "Artist_id" INT   NOT NULL,
    "image" VARCHAR   NOT NULL,
    "Biography" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Artist" PRIMARY KEY (
        "Artist_id"
     )
);

ALTER TABLE "Artwork" ADD CONSTRAINT "fk_Artwork_Artist_id" FOREIGN KEY("Artist_id")
REFERENCES "Artist" ("Artist_id");

ALTER TABLE "Artwork" ADD CONSTRAINT "fk_Artwork_Dept_id" FOREIGN KEY("Dept_id")
REFERENCES "Department" ("Dept_id");

