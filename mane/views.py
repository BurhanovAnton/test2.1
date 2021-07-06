import datetime

from django.shortcuts import render


def main(request):
    context={
        'albums': [
            {
                'image': 'https://st2.depositphotos.com/1064024/10769/i/600/depositphotos_107694484-stock-photo-little-boy.jpg',
                'description': 'картинка',
                'date': datetime.datetime.now(),
                'id': 1
            },
            {
                'image': 'https://st2.depositphotos.com/1064024/10769/i/600/depositphotos_107694484-stock-photo-little-boy.jpg',
                'description': 'картинка',
                'date': datetime.datetime.now(),
                'id': 2
            },
            {
                'image': 'https://st2.depositphotos.com/1064024/10769/i/600/depositphotos_107694484-stock-photo-little-boy.jpg',
                'description': 'картинка',
                'date': datetime.datetime.now(),
                'id': 3
            },
            {
                'image': 'https://st2.depositphotos.com/1064024/10769/i/600/depositphotos_107694484-stock-photo-little-boy.jpg',
                'description': 'картинка',
                'date': datetime.datetime.now(),
                'id': 4
            },
            {
                'image': 'https://st2.depositphotos.com/1064024/10769/i/600/depositphotos_107694484-stock-photo-little-boy.jpg',
                'description': 'картинка',
                'date': datetime.datetime.now(),
                'id': 5
            },
            {
                'image': 'https://st2.depositphotos.com/1064024/10769/i/600/depositphotos_107694484-stock-photo-little-boy.jpg',
                'description': 'картинка',
                'date': datetime.datetime.now(),
                'id': 6
            },

        ]
    }
    return render(request, 'mane/index.html', context)
