import asyncio
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from .serializers import SectorSerializer,RegisterSerializer,LogoutSerializer
from .news import fetch_news
from .ai import analyze_market
from .models import User
from rest_framework.generics import CreateAPIView

class RegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]

class AnalyzeSectorView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    def get(self, request, sector):
        serializer = SectorSerializer(data={"sector": sector})
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        sector = serializer.validated_data["sector"]
        try:
            news = asyncio.run(fetch_news(sector))
            if not news:
                news = [
                    {
                        "title": f"{sector} sector in India is growing",
                        "source": "N/A",
                        "description": "General market trends indicate growth"
                    },
                    {
                        "title": f"Investment opportunities in {sector}",
                        "source": "N/A",
                        "description": "Investors are showing interest"
                    }
                ]
            report = analyze_market(sector, news)
            request.session['last_sector'] = sector
            return Response({
                "sector": sector,
                "report": report
            })
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_205_RESET_CONTENT
        )