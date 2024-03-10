import argparse
import signal
import time

running = True
start_time = None
cnt = 1

def handle_signal(signum, frame):
    global running, cnt
    elapsed_time = time.time() - start_time
    #print(f"\nOtrzymano sygnal {signum}. Czas dzialania: {elapsed_time:.2f} sekund.")
    print(f'{cnt:d} Fibonnaci numbers generated. Exiting.')
    running = False

def main():
    global start_time, cnt

    parser = argparse.ArgumentParser(description='Drukuje liczbe sekund, ktore uplynely od uruchomienia.')
    parser.add_argument('-d', '--duration', type=int, default=10, help='Liczba sekund, po ktorej program ma sie zatrzymac.')
    args = parser.parse_args()

    # Set up signal handler
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, lambda signum, frame: print('Crtl+C nie konczy programu.'))

    start_time = time.time()

    fn1 = 0
    fn2 = 1
    
    while running :#and (time.time() - start_time) < args.duration:
        elapsed_time = time.time() - start_time
        fib_num = fn1+fn2
        #print(fn1, fn2, fib_num)
        print(fib_num)
        fn1 = fn2
        fn2 = fib_num
        cnt += 1
        #fn2 += fn1
        time.sleep(0.5)

    print("Zakonczono dzialanie programu.")

if __name__ == '__main__':
    main()
