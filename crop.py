# Function to crop 19 MP image to desired shape.

def crop_19_mp(image):
    output_image = image[365:3691, 100:4890]    # (y, x).

    return output_image


def crop_12_mp(image):
    output_image = image[360:2849, 150:3849]    # (y, x).

    return output_image


# Check image size and crop accordingly.
def crop_all(image_list):
    for i in range(len(image_list)):
        if image_list[i].size == 36000000:                  # 3000 * 4000 * 3.
            image_list[i] = crop_12_mp(image_list[i])
        elif image_list[i].size == 57517056:                # 3792 * 5056 * 3.
            image_list[i] = crop_19_mp(image_list[i])
        else:
            ValueError()
