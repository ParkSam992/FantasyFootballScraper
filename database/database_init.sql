CREATE TABLE "KeepTradeCutRanking" (
    "Id" varchar(10) NOT NULL PRIMARY KEY,
    "FirstName" varchar(50),
    "LastName" varchar(50),
    "Position" varchar(10),
    "RankingOneQB" integer,
    "RankingTwoQB" integer,
    "Resource" json,
    "UpdatedAt" timestamp
);

CREATE INDEX "KeepTradeCutRanking_IND1" ON "KeepTradeCutRanking" ("FirstName", "LastName");

CREATE INDEX "KeepTradeCutRanking_IND2" ON "KeepTradeCutRanking" ("RankingOneQB", "RankingTwoQB");