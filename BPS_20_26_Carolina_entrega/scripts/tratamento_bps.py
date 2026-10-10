from pathlib import Path
import pandas as pd

ANO_INICIAL = 2020
ANO_FINAL = 2026
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

COLUNAS_NUMERICAS = [
    "qt_medicamento", "vl_capacidade", "vl_preco_unitario", "vl_preco_total"
]
COLUNAS_DATA = ["dt_compra", "dt_insercao"]


def ler_bases():
    bases = []
    schemas = {}
    for ano in range(ANO_INICIAL, ANO_FINAL + 1):
        arquivo = RAW_DIR / f"{ano}.csv"
        if not arquivo.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")
        df = pd.read_csv(arquivo, sep=";", encoding="utf-8-sig", low_memory=False)
        df["ano_origem"] = ano
        bases.append(df)
        schemas[ano] = list(df.columns)
    return bases, schemas


def validar_schema(schemas):
    referencia = schemas[ANO_INICIAL]
    divergencias = {}
    for ano, colunas in schemas.items():
        if colunas != referencia:
            divergencias[ano] = {
                "faltantes": sorted(set(referencia) - set(colunas)),
                "extras": sorted(set(colunas) - set(referencia)),
                "ordem_diferente": colunas != referencia,
            }
    return divergencias


def tratar(df):
    # Padroniza datas em ISO. Datas inválidas são convertidas para NaT.
    for coluna in COLUNAS_DATA:
        df[coluna] = pd.to_datetime(
            df[coluna], dayfirst=True, errors="coerce"
        ).dt.strftime("%Y-%m-%d")

    # Garante tipos numéricos para quantidade e valores monetários.
    for coluna in COLUNAS_NUMERICAS:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

    # Mantém campos textuais vazios como NA, sem substituir por zero.
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # Não remove registros automaticamente: co_seq_bps é usado como identificador.
    # Duplicidades são avaliadas antes e depois da concatenação.
    return df


def main():
    bases, schemas = ler_bases()
    divergencias = validar_schema(schemas)
    if divergencias:
        print("Divergências de schema encontradas:")
        print(divergencias)
    else:
        print("Schemas dos 7 anos: compatíveis.")

    bases = [tratar(df) for df in bases]
    consolidada = pd.concat(bases, ignore_index=True)

    # Validações de integridade.
    if consolidada["co_seq_bps"].duplicated().any():
        raise ValueError("Existem duplicidades em co_seq_bps após a concatenação.")
    if (consolidada["qt_medicamento"] < 0).any():
        raise ValueError("Existem quantidades negativas.")
    if (consolidada["vl_preco_total"] < 0).any():
        raise ValueError("Existem preços totais negativos.")

    # A coluna ano_origem é mantida para auditoria da origem do arquivo.
    arquivo_saida = PROCESSED_DIR / "BPS_20_26_Carolina.csv"
    consolidada.to_csv(arquivo_saida, sep=";", index=False, encoding="utf-8-sig")

    # Versão enxuta para o dashboard, reduzindo o tamanho do arquivo.
    colunas_dashboard = [
        "ano_compra", "dt_compra", "sg_uf", "ds_item", "no_fornecedor",
        "no_fabricante", "qt_medicamento", "no_instituicao", "no_municipio",
        "modalidade", "vl_preco_unitario", "vl_preco_total", "co_seq_bps"
    ]
    arquivo_dashboard = PROCESSED_DIR / "BPS_20_26_Carolina_Dashboard.csv"
    consolidada[colunas_dashboard].to_csv(
        arquivo_dashboard, sep=";", index=False, encoding="utf-8-sig"
    )

    print(f"Registros consolidados: {len(consolidada):,}")
    print(f"Base consolidada: {arquivo_saida}")
    print(f"Base dashboard: {arquivo_dashboard}")


if __name__ == "__main__":
    main()
