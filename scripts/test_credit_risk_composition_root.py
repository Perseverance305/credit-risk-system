from app.composition_root import create_credit_risk_engine


def main() -> None:
    engine = create_credit_risk_engine()

    assert engine is not None

    print("Credit risk composition root test passed!")


if __name__ == "__main__":
    main()
