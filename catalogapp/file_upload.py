from django.core.files import File
import os

from catalogapp.models import Place, ImagePlace, ImageArea, Area, ImageWelcomeZone, WelcomeZone, ImageTerritory, \
     ImageOutsiteReg, OutsiteRegistration


class FileLoad:
    @staticmethod
    def upload_images_for_model(model_class, fk_field, model_instance, request, array_img):
        if request.data.get(array_img):
            dir_names = request.data[array_img]
            if not isinstance(dir_names, list):
                raise TypeError(f"Expected a list of string, but received a string: [{dir_names}]")
            site_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/' + 'filepond-temp-uploads'

            for dir_name in dir_names:

                files = os.listdir(os.path.join(site_root, dir_name))

                for file in files:
                    path = os.path.join(site_root, dir_name, str(file))
                    # Open the file using Django's File class
                    with open(path,
                              'rb') as image_file:  # where path is file path djangoeventforme/backend/backendeventforme/backend/filepond-temp-uploads/B2XGPLn8oiCZUVtt7fk5Hg/MjdewBMemeNSPx2BadKMYK
                        # Create a Django File object
                        django_file = File(image_file)
                        print(django_file, 'django file')

                        image_model = model_class(**{fk_field: model_instance})
                        image_model.image.save(file, django_file, save=True)
            return True
        return False

    def move_upload_img_for_place(self, request, array_img, place_id):
        return self.upload_images_for_model(model_class=ImagePlace, fk_field='place',
                                            model_instance=Place.objects.get(id=place_id),
                                            request=request, array_img=array_img)

    def move_upload_img_for_area(self, request, array_img, area_id):
        return self.upload_images_for_model(model_class=ImageArea, fk_field='area',
                                            model_instance=Area.objects.get(id=area_id),
                                            request=request, array_img=array_img)

    def move_upload_img_for_welcome_zone(self, request, array_img, zone_id):
        return self.upload_images_for_model(model_class=ImageWelcomeZone, fk_field='welcome_zone',
                                            model_instance=WelcomeZone.objects.get(id=zone_id),
                                            request=request, array_img=array_img)

    def move_upload_img_for_territory(self, request, array_img, territory_id):
        return self.upload_images_for_model(model_class=ImageTerritory, fk_field='territory',
                                            model_instance=Place.objects.get(id=territory_id),
                                            request=request, array_img=array_img)

    def move_upload_img_for_out_reg(self, request, array_img, out_reg_id):
        return self.upload_images_for_model(model_class=ImageOutsiteReg, fk_field='outsite_reg',
                                            model_instance=OutsiteRegistration.objects.get(id=out_reg_id),
                                            request=request, array_img=array_img)

    def delete_filepond_temp(self):
        pass
