import csv
import sys
import matplotlib.pyplot as plt 

def estimate_price(mileage, theta0, theta1):
    return float(theta0) + float(theta1) * float(mileage)

def write_to_txt(theta0, theta1):
    f = open("thetas.txt", "w")
    f.write(f"Theta0:{theta0}\nTheta1:{theta1}\n")
    f.close()

def reset_thetas():
    f = open("thetas.txt", "w")
    f.write(f"Theta0:0\nTheta1:0\n")
    f.close()

def parse_csv():
    data_list = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append({'km': float(row['km']), 'price': float(row['price'])})
    return data_list

def estimate_precision(theta0, theta1, data_dict):
    mae = 0 # Mean absolute error https://en.wikipedia.org/wiki/Mean_absolute_error
    for item in data_dict:
        mae += abs(estimate_price(item["km"], theta0, theta1) - item["price"])
    mae /= len(data_dict)
    print(mae)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-c":
        reset_thetas()
        return
        
    data_dict = parse_csv()
    
    m = 0
    c = 0
    c_tmp = 1
    m_tmp = 1

    L0 = 0.01
    L1 = 0.0000000001

    prev_cost = float('inf')
    tol = 1e-6

    while abs(c - c_tmp) + abs(m - m_tmp) > 0.00001:
        c_tmp = sum(estimate_price(item['km'], c, m) - item['price'] for item in data_dict)
        m_tmp = sum((estimate_price(item['km'], c, m) - item['price']) * item['km'] for item in data_dict)

        c = c - L0 * (1/len(data_dict)) * c_tmp
        m = m - L1 * (1/len(data_dict)) * m_tmp

        current_cost = sum((float(estimate_price(item['km'], c, m)) - int(item['price']))**2 for item in data_dict)

        if abs(current_cost - prev_cost) < tol:
            break
        prev_cost = current_cost

    write_to_txt(c, m)

    if len(sys.argv) > 1:
        if sys.argv[1] == "-d" or sys.argv[1] == "-l":
            plt.figure(1)
            plt.plot([data['km'] for data in data_dict], [data['price'] for data in data_dict], 'o')
            if sys.argv[1] == "-l":
                plt.plot([0, 250000], [(estimate_price(0, c, m)),(estimate_price(250000, c, m))], '-m')
            plt.grid(True)
            plt.show()
            plt.close()
        if sys.argv[1] == "-p":
            estimate_precision(c, m, data_dict)

if __name__ == "__main__":
    main()