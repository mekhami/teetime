from teetime.models import Product, Category, Feature, Job, Client, JobState, Department, Employee
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import datetime
from faker import Factory
import random
import decimal

fake = Factory.create()


class Command(BaseCommand):
    help = 'makes a dummy company using fake Factory'
    def handle(self, *args, **options):
        t = datetime.date.today()

        # states
        for i in ['new', 'art review', 'art approved', 'inventory ready', 'ready to ship', 'delivered']:
            o, c = JobState.objects.get_or_create(name=i)
            if c:
                print 'created: {0}'.format(o)

        # departments
        for i in ['art', 'hr', 'owner', 'intern', 'reception', 'production']:
            o, c = Department.objects.get_or_create(name=i)
            if c:
                print 'created: {0}'.format(o)

        # features
        for i in range(100):
            o, c = Feature.objects.get_or_create(
                    name=fake.color_name(),
                    attribute='Color',
                )
            if c:
                print 'created: {0}'.format(o)

        # categories
        for i in ['top', 'bottom', 'coosie', 'kercheif', 'hat', 'tote', 'cape']:
            o, c = Category.objects.get_or_create(name=i)
            if c:
                print 'created: {0}'.format(o)

        # clients
        for i in range(50):
            o, c = Client.objects.get_or_create(
                    name=fake.company(),
                    address=fake.address(),
                    email=fake.company_email(),
                )
            if c:
                print 'created: {0}'.format(o)

        # jobs
        for i in range(100):
            o, c = Job.objects.get_or_create(
                    name=fake.word(),
                    client=Client.objects.all().order_by('?')[0],
                    description=fake.sentences(nb=3),
                    state=JobState.objects.all().order_by('?')[0],
                )
            if c:
                print 'created: {0}'.format(o)

        # products
        for i in range(100):
            o, c = Product.objects.get_or_create(
                    category=Category.objects.all().order_by('?')[0],
                    job=Job.objects.all().order_by('?')[0],
                    price=decimal.Decimal('%d.%d' % (random.randint(0,100),random.randint(0,10))),
                    name=fake.word(),
                )
            if c:
                print 'created: {0}'.format(o)

        # employees
        for i in range(30):
            fn = fake.first_name()
            ln = fake.last_name()
            o, c = Employee.objects.get_or_create(
                    user=User.objects.create(
                        first_name=fn,
                        last_name=ln,
                        username='{0}{1}'.format(fn[0], ln,),
                        email=fake.company_email(),
                    ),
                    department=Department.objects.all().order_by('?')[0],
            )
            if c:
                print 'created: {0}'.format(o)

    print 'done'
