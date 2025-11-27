# first make know values global like prome number and the ganerator (base)
# then make function where allice compute the its value send it , to bob
# also same fuction for bob , why not only one fuction that handles both or mean same fuction computes for both by picking random secret number for both
# then comes the main fuction we we calculate back the exact same key for both
# or can use threading for this to make process seemless lik computing for alice and bomb at same time using single method like and same for getting the key back
import random
import threading
import time
from sympy import nextprime

# --- 1. GLOBAL PUBLIC VALUES (The Constants) ---
# Everyone (including Eve) knows these.
PRIME = nextprime(random.getrandbits(1024))      # The Clock
GENERATOR = 5   # The Base

# Shared memory to store the results from the threads
public_keys = {}
shared_secrets = {}

# --- 2. THE UNIVERSAL FUNCTION (DRY Principle) ---
def compute_keys(person_name):
    print(f"[{person_name}] Generating Secret Key...")

    # 1. Pick a random secret number
    secret_key = random.randint(1, 20)

    # Simulate "Work" (Network/CPU delay)
    time.sleep(1)

    # 2. Calculate Public Key: (g ^ secret) % p
    # Python's pow(base, exp, mod) is faster than (base ** exp) % mod
    public_key = pow(GENERATOR, secret_key, PRIME)

    print(f"[{person_name}] My Secret is {secret_key}. Broadcasting Public Key: {public_key}")

    # Save public key to the "Network" (Dictionary)
    public_keys[person_name] = public_key

    # Return secret so we can use it later for the final step
    return secret_key

# --- 3. THE THREADING EXECUTION ---
def simulate_exchange():
    print("--- STARTING SECURE HANDSHAKE (THREADED) ---")

    # Create Threads for Alice and Bob
    # We use a wrapper to capture the return values (Secret Keys)
    alice_secret_storage = []
    bob_secret_storage = []

    def alice_job():
        alice_secret_storage.append(compute_keys("Alice"))

    def bob_job():
        bob_secret_storage.append(compute_keys("Bob"))

    t1 = threading.Thread(target=alice_job)
    t2 = threading.Thread(target=bob_job)

    # Start them simultaneously!
    t1.start()
    t2.start()

    # Wait for both to finish before continuing
    t1.join()
    t2.join()

    print("\n--- PUBLIC KEYS EXCHANGED ON NETWORK ---")
    print(f"Network sees: {public_keys}\n")

    # --- 4. THE FINAL CALCULATION (Getting the Shared Secret) ---

    # Alice calculates: (Bob's Public Key ^ Alice's Secret) % P
    alice_s = alice_secret_storage[0]
    bob_p = public_keys["Bob"]
    alice_final = pow(bob_p, alice_s, PRIME)

    # Bob calculates: (Alice's Public Key ^ Bob's Secret) % P
    bob_s = bob_secret_storage[0]
    alice_p = public_keys["Alice"]
    bob_final = pow(alice_p, bob_s, PRIME)

    print(f"Alice's Calculated Shared Key: {alice_final}")
    print(f"Bob's Calculated Shared Key:   {bob_final}")

    if alice_final == bob_final:
        print("\n✅ SUCCESS: Connection Encrypted.")
    else:
        print("\n❌ ERROR: Math failed.")

# Run the simulation
simulate_exchange()
