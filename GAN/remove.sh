for var in {2551..3000}
do
    python test.py -l 1260 -i './ASL dataset/asl_alphabet_train/asl_alphabet_train/S/S'$var'.jpg' -o ./imgs_outputs
done

for var in {2551..3000}
do
    python test.py -l 1260 -i './ASL dataset/asl_alphabet_train/asl_alphabet_train/E/E'$var'.jpg' -o ./imgs_outputs
done


python test.py -l 1260 -i './ASL dataset/asl_alphabet_train/asl_alphabet_train/S/S1.jpg' -o ./imgs_outputs