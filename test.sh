DATASET_PATH="datasets/nerf_llff_data/$1"

if [ -z $2 ]
then
    quality_type="high"
fi

if [ -n $2 ]
then
    quality_type=$2
fi

python Geolocation.py $1
colmap automatic_reconstructor \
    --image_path $DATASET_PATH/images \
    --workspace_path $DATASET_PATH \
    --use_gpu 1 \
    --gpu_index "0,1" \
    --quality $quality_type

python img2poses.py $1
python image_resize.py $1
python stage1_hash.py $1
python stage2_hash.py $1

if [ -z $3 ]
then
    python stage3_hash.py $1
fi

if [ $3=="crop" ]
then
    python stage3_hash.py $1
fi

if  [ $3=="entire" ]
then
    python stage3_with_box_hash.py $1
fi