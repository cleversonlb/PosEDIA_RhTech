create database "database-rhtech";

CREATE TABLE "Colaboradores" (
	"id" serial NOT NULL,
	"Nome" VARCHAR(255) NOT NULL,
	"salario" FLOAT NOT NULL,
	"id_escolaridade" integer NOT NULL,
	"id_departamento" integer NOT NULL,
	CONSTRAINT "Colaboradores_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Departamento" (
	"id" serial NOT NULL,
	"Departamento" VARCHAR(255) NOT NULL,
	"id_colaborador" integer NOT NULL,
	CONSTRAINT "Departamento_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "NF" (
	"id" serial NOT NULL,
	"numero" integer NOT NULL,
	"dados" VARCHAR(255) NOT NULL,
	"id_empresa" integer NOT NULL,
	"valor" FLOAT NOT NULL,
	CONSTRAINT "NF_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Empresa" (
	"id" serial NOT NULL,
	"empresa" VARCHAR(255) NOT NULL,
	CONSTRAINT "Empresa_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Escolaridade" (
	"id" serial NOT NULL,
	"escolaridade" VARCHAR(255) NOT NULL,
	CONSTRAINT "Escolaridade_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Folha_Pagamento" (
	"id" serial NOT NULL,
	"id_colaborador" integer NOT NULL,
	"valor hora extra" decimal NOT NULL,
	CONSTRAINT "Folha_Pagamento_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Departamento_empresa" (
	"id" serial NOT NULL,	
	"id_empresa" integer NOT NULL,
	"id_departamento" integer NOT null,
	CONSTRAINT "Departamento_empresa_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Ponto" (
	"id" serial NOT NULL,
	"data entrada" serial NOT NULL,
	"data saida" serial NOT NULL,
	"id_colaborador" integer NOT NULL,
	CONSTRAINT "Ponto_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "Colaboradores"  ADD CONSTRAINT "Colaboradores_fk0" FOREIGN KEY ("id_escolaridade") REFERENCES "Escolaridade"("id");
ALTER TABLE "Colaboradores" ADD CONSTRAINT "Colaboradores_fk1" FOREIGN KEY ("id_departamento") REFERENCES "Departamento"("id");

ALTER TABLE "Departamento" ADD CONSTRAINT "Departamento_fk0" FOREIGN KEY ("id_colaborador") REFERENCES "Colaboradores"("id");

ALTER TABLE "NF" ADD CONSTRAINT "NF_fk0" FOREIGN KEY ("id_empresa") REFERENCES "Empresa"("id");



ALTER TABLE "Folha_Pagamento" ADD CONSTRAINT "Folha_Pagamento_fk0" FOREIGN KEY ("id_colaborador") REFERENCES "Colaboradores"("id");

ALTER TABLE "Departamento_empresa" ADD CONSTRAINT "Departamento_empresa_fk0" FOREIGN KEY ("id_empresa") REFERENCES "Empresa"("id");
ALTER TABLE "Departamento_empresa" ADD CONSTRAINT "Departamento_empresa_fk1" FOREIGN KEY ("id_departamento") REFERENCES "Departamento"("id");

ALTER TABLE "Ponto" ADD CONSTRAINT "Ponto_fk0" FOREIGN KEY ("id_colaborador") REFERENCES "Colaboradores"("id");
