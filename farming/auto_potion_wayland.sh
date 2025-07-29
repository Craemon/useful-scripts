#!/bin/bash
sleep 10

run_count=0  # Counter for total potion uses
wait_time=2100  # 35 minutes (in seconds)

while true; do
    sudo ydotool click --hold 272  # Hold right mouse button (button 3 = 272 in Linux input event codes)
    sleep 2
    sudo ydotool click --release 272  # Release right mouse button
    sleep 5  # Waits for the drinking animation

    # Increase run count
    ((run_count++))
    echo "Potion drunk! Total runs: $run_count"

    # Countdown timer
    for ((i=wait_time; i>0; i--)); do
        echo -ne "Next potion in: $i seconds\r"
        sleep 1
    done
    echo ""  # Clear the line after countdown
done

