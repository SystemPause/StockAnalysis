declare -a emailAddresses=("alessandrospeggiorin@gmail.com")
declare -a screenerUrls=("undervalued_large_caps" "most_actives" "day_gainers" "day_losers")


# Get all the stock info and save them as files. 
for url in "${screenerUrls[@]}"
do
    echo $url
    python3 Main.py auto "https://finance.yahoo.com/screener/predefined/${url}"
done

# Send the email containing the files
# But first merge them all 
cat *.txt >> mergedFiles.txt
for email in "${emailAddresses[@]}"
do
    echo "" | mail -s "Daily Stock Analysis" $email < mergedFiles.txt
done

# Clean up generated files
rm *.txt

  