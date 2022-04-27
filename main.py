import random
import lotto_balls
import power_ball


def main():

    num_of_tickets = input("Enter the number of tickets: ")

    for i in range(int(num_of_tickets)):

        print("\n")
        print("ticket no " , (i+1))

        for i in range(5):

            lb = lotto_balls.lotto_balls('Ball: '+str(i+1)+": "  ,random.randint(1, 69))
            print(lb.name, lb.num)

        pb = power_ball.power_ball('Powerball', random.randint(1, 26))
        print(pb.name, pb.num)


if __name__ == "__main__":
    main()
