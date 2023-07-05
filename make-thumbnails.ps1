# Get-ChildItem -Directory | ForEach-Object {
#     Get-ChildItem $_.FullName -Filter *.jpg | ForEach-Object {
#         python .\make-thumbnail.py $_.FullName
#         # Write-Output $_.FullName
#     }
# }
