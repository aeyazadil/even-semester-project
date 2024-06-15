import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request,'index1.html')

def institute_chart(request):
    # Example data

    # Create DataFrame
    df = pd.read_csv("data/seat_allotment_results.csv")

    # Drop duplicates based on 'Institute' and 'Year'
    df_unique = df.drop_duplicates(subset=['Institute', 'Year'])

    # Group by 'Institute Type' and 'Year', then count unique 'Institute'
    grouped = df_unique.groupby(['Institute Type', 'Year']).size().reset_index(name='Count')

    # Pivot the data for plotting
    pivot_df = grouped.pivot(index='Year', columns='Institute Type', values='Count').fillna(0)

    # Prepare data for Chart.js
    chart_data = {
        'labels': pivot_df.index.tolist(),
        'datasets': []
    }

    colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']
    for idx, institute_type in enumerate(pivot_df.columns):
        chart_data['datasets'].append({
            'label': institute_type,
            'data': pivot_df[institute_type].tolist(),
            'backgroundColor': colors[idx % len(colors)],
        })

    return render(request, 'webpages/institute.html', {
        'chart_data': chart_data
    })

def rank(request):
    return render(request,'webpages/rank.html')

def institute_rank(request):
    return render(request,'webpages/institute_rank.html')

def program(request):
    return render(request,'webpages/program.html')

def popular_institute(request):
    return render(request,'webpages/popular_institute.html')

def popular_course(request):
    return render(request,'webpages/popular_course.html')

def degree(request):
    return render(request,'webpages/degree.html')

def quota(request):
    return render(request,'webpages/quota.html')

def get_quota(request):

    seat_type = request.POST.get('seat_type')
    year = int(request.POST.get('year'))
    institute = request.POST.get('institute')
    gender = request.POST.get('gender')

    df = pd.read_csv("data/seat_allotment_results.csv")


    filtered_df = df[(
                             (df['Seat Type'] == seat_type) &
                             (df["Institute"] == institute) &
                             (df['Year'] == year)&(df['Academic Program Name'] != "Architecture (5 Years, Bachelor of Architecture)"))]    

            

    if gender == 'Gender-Neutral':
                filtered_df = filtered_df[filtered_df['Gender-Neutral'] == 1]
    else:
                filtered_df = filtered_df[filtered_df['Female'] == 1]
    os_df = filtered_df[filtered_df["Quota"]=="OS"]
    top_10_programs = os_df.nsmallest(10, 'Closing Rank')["Academic Program Name"].tolist()
    filtered_df = filtered_df[((filtered_df['Quota']=="HS")|(filtered_df['Quota']=="OS"))]

    filtered_df = filtered_df[filtered_df['Academic Program Name'].isin(top_10_programs)]

    pivot_df = filtered_df.pivot(index='Academic Program Name', columns='Quota', values='Closing Rank')

    # Reindex the pivot table to ensure the institutes are in the same order
    pivot_df = pivot_df.reindex(top_10_programs).fillna(0)
    chart_data = {
        'labels': pivot_df.index.tolist(),
        'datasets': [
            {
                'label': 'Other State',
                'data': pivot_df['OS'].tolist() if 'OS' in pivot_df.columns else [],
                'backgroundColor': '#E74C3C',
            },
            {
                'label': 'Home State',
                'data': pivot_df['HS'].tolist() if 'HS' in pivot_df.columns else [],
                'backgroundColor': '#3498DB',
            }
        ]
    }

    return JsonResponse(chart_data)



def get_degree(request):
  
    df = pd.read_csv("data/seat_allotment_results.csv")

    year = int(request.POST.get('year'))
    inst_type =request.POST.get('inst_type')

    filtered_df = df[(df["Year"]==year)&(df["Institute Type"]==inst_type)]
    df_unique = filtered_df.drop_duplicates(subset=['Institute', 'Academic Program Name'])
    unique_program_counts = filtered_df.groupby('Institute')['Academic Program Name'].nunique()

    # Sort the values to get the top 10 largest counts
    top_10_institutes = unique_program_counts.nlargest(10).index.tolist()



    largest = df_unique.groupby(['Institute','Degree']).size().reset_index(name='Count')
    largest = largest[largest["Institute"].isin(top_10_institutes)]

    pivot_df = largest.pivot(index='Institute', columns='Degree', values='Count').fillna(0).reindex(top_10_institutes)
    total_degree_counts = pivot_df.sum(axis=0)

    # Sort the degrees in descending order based on the total count
    sorted_degrees = total_degree_counts.sort_values(ascending=False).index

    # Rearrange the columns in the pivot DataFrame based on the sorted degrees
    pivot_df = pivot_df[sorted_degrees]
    # Prepare data for Chart.js
    chart_data = {
        'labels': pivot_df.index.tolist(),
        'datasets': []
    }

    colors = ["#003f5c","#58508d","#8a508f","#bc5090","#de5a79","#ff6361","#ff8531","#ffa600"]
    for idx, institute_type in enumerate(pivot_df.columns):
        chart_data['datasets'].append({
            'label': institute_type,
            'data': pivot_df[institute_type].tolist(),
            'backgroundColor': colors[idx % len(colors)],
        })

    
    return JsonResponse(chart_data)
   



def get_popular_course(request):
    if request.method == 'POST':
        try:
            df = pd.read_csv("data/seat_allotment_results.csv")


            institute_type = request.POST.get('institute_type')
            seat_type = request.POST.get('seat_type')
            year = request.POST.get('year')
            institute = request.POST.get('institute')
            gender = request.POST.get('gender')

            
            

            year = int(year)

            if institute == "ALL":
                filtered_df = df[(df['Institute Type'] == institute_type) &
                             (df['Seat Type'] == seat_type) &
                             (df['Year'] == year)&
                             ((df['Quota']=='AI')|(df['Quota']=='OS')
                              )&(df['Academic Program Name'] != "Architecture (5 Years, Bachelor of Architecture)")
                              &(df['Academic Program Name'] != "Planning (4 Years, Bachelor of Planning)")]
            else:
                filtered_df = df[
                             (df['Seat Type'] == seat_type) &
                             (df["Institute"] == institute) &
                             (df['Year'] == year)&
                             ((df['Quota']=='AI')|(df['Quota']=='OS')) &
                             (df['Academic Program Name'] != "Architecture (5 Years, Bachelor of Architecture)")]    

            

            if gender == 'Gender-Neutral':
                filtered_df = filtered_df[filtered_df['Gender-Neutral'] == 1]
            else:
                filtered_df = filtered_df[filtered_df['Female'] == 1]

           

            preparatory_zero = filtered_df[filtered_df['Preparatory_CR'] == 0]
            preparatory_one = filtered_df[filtered_df['Preparatory_CR'] == 1]

            # Get the smallest 10 from preparatory_zero, and if needed, fill with preparatory_one
            top_10_preparatory_zero = preparatory_zero.nsmallest(10, 'Closing Rank')
            remaining_slots = 10 - len(top_10_preparatory_zero)
            if remaining_slots > 0:
                top_10_preparatory_one = preparatory_one.nsmallest(remaining_slots, 'Closing Rank')
                top_10 = pd.concat([top_10_preparatory_zero, top_10_preparatory_one])
            else:
                top_10 = top_10_preparatory_zero

# Ensure top_10 is sorted by Closing Rank
            

            data = {
                'institutes': top_10['Institute'].tolist(),
                'ranks': top_10['Closing Rank'].tolist(),
                'programs':top_10['Academic Program Name'].tolist(),
                'is_preparatory': top_10['Preparatory_CR'].tolist()
            }

            return JsonResponse(data)
        except Exception as e:
            # Log the exception
            print(f"Error: {e}")
            return JsonResponse({'error': 'An error occurred'}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_popular_institute(request):
    if request.method == 'POST':
        try:
            df = pd.read_csv("data/seat_allotment_results.csv")

           

            institute_type = request.POST.get('institute_type')
            seat_type = request.POST.get('seat_type')
            year = request.POST.get('year')
            academic_program = request.POST.get('academic_program')
            gender = request.POST.get('gender')

            # Check for missing data in POST request
            if not all([institute_type, seat_type, year, academic_program, gender]):
                return JsonResponse({'error': 'Missing parameters'}, status=400)

            year = int(year)

            filtered_df = df[(df['Institute Type'] == institute_type) &
                             (df['Seat Type'] == seat_type) &
                             (df["Academic Program Name"] == academic_program) &
                             (df['Year'] == year)&
                             ((df['Quota']=='AI')|(df['Quota']=='OS'))]

            if gender == 'Gender-Neutral':
                filtered_df = filtered_df[filtered_df['Gender-Neutral'] == 1]
            else:
                filtered_df = filtered_df[filtered_df['Female'] == 1]

           

            preparatory_zero = filtered_df[filtered_df['Preparatory_CR'] == 0]
            preparatory_one = filtered_df[filtered_df['Preparatory_CR'] == 1]

            # Get the smallest 10 from preparatory_zero, and if needed, fill with preparatory_one
            top_10_preparatory_zero = preparatory_zero.nsmallest(10, 'Closing Rank')
            remaining_slots = 10 - len(top_10_preparatory_zero)
            if remaining_slots > 0:
                top_10_preparatory_one = preparatory_one.nsmallest(remaining_slots, 'Closing Rank')
                top_10 = pd.concat([top_10_preparatory_zero, top_10_preparatory_one])
            else:
                top_10 = top_10_preparatory_zero

# Ensure top_10 is sorted by Closing Rank
            

            data = {
                'institutes': top_10['Institute'].tolist(),
                'ranks': top_10['Closing Rank'].tolist(),
                'is_preparatory': top_10['Preparatory_CR'].tolist()
            }

            return JsonResponse(data)
        except Exception as e:
            # Log the exception
            print(f"Error: {e}")
            return JsonResponse({'error': 'An error occurred'}, status=500)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_program_data(request):
    df = pd.read_csv("data/seat_allotment_results.csv")
    if request.method == 'POST':


        institute_type = request.POST.get('institute_type')
        seat_type = request.POST.get('seat_type')
        program = request.POST.get('academic_program')

        # Filter the DataFrame
        filtered_df = df[(df['Seat Type'] == seat_type) & (df['Academic Program Name'] == program)
                         &(df['Institute Type'] == institute_type)&
                             ((df['Quota']=='AI')|(df['Quota']=='OS'))]

        # Group by 'Year' and find the row with the maximum 'Closing Rank' for each group
        gn_grouped = filtered_df[filtered_df['Gender-Neutral'] == 1].groupby('Year').apply(lambda x: x.loc[x['Closing Rank'].idxmax()]).reset_index(drop=True)
        female_grouped = filtered_df[filtered_df['Female'] == 1].groupby('Year').apply(lambda x: x.loc[x['Closing Rank'].idxmax()]).reset_index(drop=True)

        # Prepare the data to send back to the frontend
        response_data = {
            'years': gn_grouped['Year'].tolist(),
            'gender_neutral_ranks': gn_grouped['Closing Rank'].tolist(),
            'female_ranks': female_grouped['Closing Rank'].tolist(),
            'gn_institutes': gn_grouped['Institute'].tolist(),
            'gn_programs': gn_grouped['Academic Program Name'].tolist(),
            'female_institutes': female_grouped['Institute'].tolist(),
            'female_programs': female_grouped['Academic Program Name'].tolist(),
        }

        return JsonResponse(response_data)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_institute_data(request):
    df = pd.read_csv("data/seat_allotment_results.csv")
    if request.method == 'POST':

        
        seat_type = request.POST.get('seat_type')
        institute_name = request.POST.get('institute_name')

        # Filter the DataFrame
        filtered_df = df[(df['Seat Type'] == seat_type) & (df['Institute'] == institute_name)&
                             ((df['Quota']=='AI')|(df['Quota']=='OS'))]

        # Group by 'Year' and find the row with the maximum 'Closing Rank' for each group
        gn_grouped = filtered_df[filtered_df['Gender-Neutral'] == 1].groupby('Year').apply(lambda x: x.loc[x['Closing Rank'].idxmax()]).reset_index(drop=True)
        female_grouped = filtered_df[filtered_df['Female'] == 1].groupby('Year').apply(lambda x: x.loc[x['Closing Rank'].idxmax()]).reset_index(drop=True)

        # Prepare the data to send back to the frontend
        response_data = {
            'years': gn_grouped['Year'].tolist(),
            'gender_neutral_ranks': gn_grouped['Closing Rank'].tolist(),
            'female_ranks': female_grouped['Closing Rank'].tolist(),
            'gn_institutes': gn_grouped['Institute'].tolist(),
            'gn_programs': gn_grouped['Academic Program Name'].tolist(),
            'female_institutes': female_grouped['Institute'].tolist(),
            'female_programs': female_grouped['Academic Program Name'].tolist(),
        }

        return JsonResponse(response_data)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_data(request):

    df = pd.read_csv("data/seat_allotment_results.csv")
    if request.method == 'POST':


        institute_type = request.POST.get('institute_type')
        seat_type = request.POST.get('seat_type')

        # Filter the DataFrame
        filtered_df = df[(df['Institute Type'] == institute_type) & (df['Seat Type'] == seat_type)&
                             ((df['Quota']=='AI')|(df['Quota']=='OS'))]

        # Group by 'Year' and find the row with the maximum 'Closing Rank' for each group
        gn_grouped = filtered_df[filtered_df['Gender-Neutral'] == 1].groupby('Year').apply(lambda x: x.loc[x['Closing Rank'].idxmax()]).reset_index(drop=True)
        female_grouped = filtered_df[filtered_df['Female'] == 1].groupby('Year').apply(lambda x: x.loc[x['Closing Rank'].idxmax()]).reset_index(drop=True)

        # Prepare the data to send back to the frontend
        response_data = {
            'years': gn_grouped['Year'].tolist(),
            'gender_neutral_ranks': gn_grouped['Closing Rank'].tolist(),
            'female_ranks': female_grouped['Closing Rank'].tolist(),
            'gn_institutes': gn_grouped['Institute'].tolist(),
            'gn_programs': gn_grouped['Academic Program Name'].tolist(),
            'female_institutes': female_grouped['Institute'].tolist(),
            'female_programs': female_grouped['Academic Program Name'].tolist(),
        }

        return JsonResponse(response_data)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def popular_institute(request):
    return render(request,'webpages/popular_institute.html')