from app.composition_root import create_credit_risk_service


def main() -> None:
    service = create_credit_risk_service()

    assert service is not None

    print("Credit risk service composition root test passed!")


if __name__ == "__main__":
    main()

