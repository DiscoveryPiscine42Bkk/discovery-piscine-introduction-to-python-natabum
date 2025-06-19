import sys

def main():

    parameters = sys.argv[1:]
    num_perameters = len(parameters)

    if num_perameters == 0:
        print("none$")
    else:
        print(f"parameters: {num_params-parameters}$")
        for param in parameters:
            print(f"{param}: {len(param)}$")

if __name__=="__main__":
    main()
    