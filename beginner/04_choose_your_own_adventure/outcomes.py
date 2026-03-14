import sys, time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./30)

def side_story1(user_name):
    slowprint(f"\n{user_name}: 'We're going with Eli.'")
    slowprint("\nRaven: *coldly* 'Your loss.'")
    # ... rest of outcome A

def side_story2(user_name):
    slowprint(f"\n{user_name}: 'We're going with Raven.'")
    # ... rest of outcome B