declare -a emailAddresses=("alessandrospeggiorin@gmail.com" "m19.massimiliano@gmail.com")
declare -a screenerUrls=("day_gainers" "day_losers" "undervalued_large_caps" "most_actives")


# Get all the stock info and save them as files. 
for url in "${screenerUrls[@]}"
do
    # Connect to vpn 
    sudo nordvpn connect 
    sudo nordvpn status
    echo $url
    python3 Main.py auto "https://uk.finance.yahoo.com/screener/predefined/${url}"
    
done

# Once done disconnect from the vpn to prevent problems with the vpn + email
sudo nordvpn disconnect

# Send the email containing the files
# But first merge them all 
cat *.txt >> mergedFiles.txt
for email in "${emailAddresses[@]}"
do
    echo "" | mail -s "Daily Stock Analysis" $email < mergedFiles.txt
done

# Clean up generated files
rm *.txt

  