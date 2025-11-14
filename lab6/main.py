from composite import create_sample_autosalon

def main():
    print("=== АВТОСАЛОН - ДЕМОНСТРАЦИЯ COMPOSITE PATTERN ===\n")

    autosalon = create_sample_autosalon()

    print("СТРУКТУРА АВТОСАЛОНА:")
    print("=" * 50)
    print(autosalon.get_description())


if __name__ == "__main__":
    main()
