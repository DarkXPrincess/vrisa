# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addr(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    fromhn = models.CharField(max_length=12, blank=True, null=True)
    tohn = models.CharField(max_length=12, blank=True, null=True)
    side = models.CharField(max_length=1, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    plus4 = models.CharField(max_length=4, blank=True, null=True)
    fromtyp = models.CharField(max_length=1, blank=True, null=True)
    totyp = models.CharField(max_length=1, blank=True, null=True)
    fromarmid = models.IntegerField(blank=True, null=True)
    toarmid = models.IntegerField(blank=True, null=True)
    arid = models.CharField(max_length=22, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addr'


class Addrfeat(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    statefp = models.CharField(max_length=2)
    aridl = models.CharField(max_length=22, blank=True, null=True)
    aridr = models.CharField(max_length=22, blank=True, null=True)
    linearid = models.CharField(max_length=22, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    lfromhn = models.CharField(max_length=12, blank=True, null=True)
    ltohn = models.CharField(max_length=12, blank=True, null=True)
    rfromhn = models.CharField(max_length=12, blank=True, null=True)
    rtohn = models.CharField(max_length=12, blank=True, null=True)
    zipl = models.CharField(max_length=5, blank=True, null=True)
    zipr = models.CharField(max_length=5, blank=True, null=True)
    edge_mtfcc = models.CharField(max_length=5, blank=True, null=True)
    parityl = models.CharField(max_length=1, blank=True, null=True)
    parityr = models.CharField(max_length=1, blank=True, null=True)
    plus4l = models.CharField(max_length=4, blank=True, null=True)
    plus4r = models.CharField(max_length=4, blank=True, null=True)
    lfromtyp = models.CharField(max_length=1, blank=True, null=True)
    ltotyp = models.CharField(max_length=1, blank=True, null=True)
    rfromtyp = models.CharField(max_length=1, blank=True, null=True)
    rtotyp = models.CharField(max_length=1, blank=True, null=True)
    offsetl = models.CharField(max_length=1, blank=True, null=True)
    offsetr = models.CharField(max_length=1, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'addrfeat'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bg(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    bg_id = models.CharField(primary_key=True, max_length=12)
    namelsad = models.CharField(max_length=13, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bg'
        db_table_comment = 'block groups'


class County(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    countyns = models.CharField(max_length=8, blank=True, null=True)
    cntyidfp = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    csafp = models.CharField(max_length=3, blank=True, null=True)
    cbsafp = models.CharField(max_length=5, blank=True, null=True)
    metdivfp = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'county'


class CountyLookup(models.Model):
    pk = models.CompositePrimaryKey('st_code', 'co_code')
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_lookup'


class CountysubLookup(models.Model):
    pk = models.CompositePrimaryKey('st_code', 'co_code', 'cs_code')
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField()
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countysub_lookup'


class Cousub(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    cousubfp = models.CharField(max_length=5, blank=True, null=True)
    cousubns = models.CharField(max_length=8, blank=True, null=True)
    cosbidfp = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    cnectafp = models.CharField(max_length=3, blank=True, null=True)
    nectafp = models.CharField(max_length=5, blank=True, null=True)
    nctadvfp = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    awater = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cousub'


class DirectionLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direction_lookup'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Edges(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    tfidl = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tfidr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    smid = models.CharField(max_length=22, blank=True, null=True)
    lfromadd = models.CharField(max_length=12, blank=True, null=True)
    ltoadd = models.CharField(max_length=12, blank=True, null=True)
    rfromadd = models.CharField(max_length=12, blank=True, null=True)
    rtoadd = models.CharField(max_length=12, blank=True, null=True)
    zipl = models.CharField(max_length=5, blank=True, null=True)
    zipr = models.CharField(max_length=5, blank=True, null=True)
    featcat = models.CharField(max_length=1, blank=True, null=True)
    hydroflg = models.CharField(max_length=1, blank=True, null=True)
    railflg = models.CharField(max_length=1, blank=True, null=True)
    roadflg = models.CharField(max_length=1, blank=True, null=True)
    olfflg = models.CharField(max_length=1, blank=True, null=True)
    passflg = models.CharField(max_length=1, blank=True, null=True)
    divroad = models.CharField(max_length=1, blank=True, null=True)
    exttyp = models.CharField(max_length=1, blank=True, null=True)
    ttyp = models.CharField(max_length=1, blank=True, null=True)
    deckedroad = models.CharField(max_length=1, blank=True, null=True)
    artpath = models.CharField(max_length=1, blank=True, null=True)
    persist = models.CharField(max_length=1, blank=True, null=True)
    gcseflg = models.CharField(max_length=1, blank=True, null=True)
    offsetl = models.CharField(max_length=1, blank=True, null=True)
    offsetr = models.CharField(max_length=1, blank=True, null=True)
    tnidf = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tnidt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'edges'


class Estacion(models.Model):
    id_e = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cert_mant = models.CharField(max_length=200, blank=True, null=True)
    cert_cal = models.CharField(max_length=200, blank=True, null=True)
    ubicacion = models.CharField(max_length=200)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    e_validacion = models.TextField()  # This field type is a guess.
    estado = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estacion'


class Faces(models.Model):
    gid = models.AutoField(primary_key=True)
    tfid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    statefp00 = models.CharField(max_length=2, blank=True, null=True)
    countyfp00 = models.CharField(max_length=3, blank=True, null=True)
    tractce00 = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce00 = models.CharField(max_length=1, blank=True, null=True)
    blockce00 = models.CharField(max_length=4, blank=True, null=True)
    cousubfp00 = models.CharField(max_length=5, blank=True, null=True)
    submcdfp00 = models.CharField(max_length=5, blank=True, null=True)
    conctyfp00 = models.CharField(max_length=5, blank=True, null=True)
    placefp00 = models.CharField(max_length=5, blank=True, null=True)
    aiannhfp00 = models.CharField(max_length=5, blank=True, null=True)
    aiannhce00 = models.CharField(max_length=4, blank=True, null=True)
    comptyp00 = models.CharField(max_length=1, blank=True, null=True)
    trsubfp00 = models.CharField(max_length=5, blank=True, null=True)
    trsubce00 = models.CharField(max_length=3, blank=True, null=True)
    anrcfp00 = models.CharField(max_length=5, blank=True, null=True)
    elsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    scsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    unsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    uace00 = models.CharField(max_length=5, blank=True, null=True)
    cd108fp = models.CharField(max_length=2, blank=True, null=True)
    sldust00 = models.CharField(max_length=3, blank=True, null=True)
    sldlst00 = models.CharField(max_length=3, blank=True, null=True)
    vtdst00 = models.CharField(max_length=6, blank=True, null=True)
    zcta5ce00 = models.CharField(max_length=5, blank=True, null=True)
    tazce00 = models.CharField(max_length=6, blank=True, null=True)
    ugace00 = models.CharField(max_length=5, blank=True, null=True)
    puma5ce00 = models.CharField(max_length=5, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    blockce = models.CharField(max_length=4, blank=True, null=True)
    cousubfp = models.CharField(max_length=5, blank=True, null=True)
    submcdfp = models.CharField(max_length=5, blank=True, null=True)
    conctyfp = models.CharField(max_length=5, blank=True, null=True)
    placefp = models.CharField(max_length=5, blank=True, null=True)
    aiannhfp = models.CharField(max_length=5, blank=True, null=True)
    aiannhce = models.CharField(max_length=4, blank=True, null=True)
    comptyp = models.CharField(max_length=1, blank=True, null=True)
    trsubfp = models.CharField(max_length=5, blank=True, null=True)
    trsubce = models.CharField(max_length=3, blank=True, null=True)
    anrcfp = models.CharField(max_length=5, blank=True, null=True)
    ttractce = models.CharField(max_length=6, blank=True, null=True)
    tblkgpce = models.CharField(max_length=1, blank=True, null=True)
    elsdlea = models.CharField(max_length=5, blank=True, null=True)
    scsdlea = models.CharField(max_length=5, blank=True, null=True)
    unsdlea = models.CharField(max_length=5, blank=True, null=True)
    uace = models.CharField(max_length=5, blank=True, null=True)
    cd111fp = models.CharField(max_length=2, blank=True, null=True)
    sldust = models.CharField(max_length=3, blank=True, null=True)
    sldlst = models.CharField(max_length=3, blank=True, null=True)
    vtdst = models.CharField(max_length=6, blank=True, null=True)
    zcta5ce = models.CharField(max_length=5, blank=True, null=True)
    tazce = models.CharField(max_length=6, blank=True, null=True)
    ugace = models.CharField(max_length=5, blank=True, null=True)
    puma5ce = models.CharField(max_length=5, blank=True, null=True)
    csafp = models.CharField(max_length=3, blank=True, null=True)
    cbsafp = models.CharField(max_length=5, blank=True, null=True)
    metdivfp = models.CharField(max_length=5, blank=True, null=True)
    cnectafp = models.CharField(max_length=3, blank=True, null=True)
    nectafp = models.CharField(max_length=5, blank=True, null=True)
    nctadvfp = models.CharField(max_length=5, blank=True, null=True)
    lwflag = models.CharField(max_length=1, blank=True, null=True)
    offset = models.CharField(max_length=1, blank=True, null=True)
    atotal = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tractce20 = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce20 = models.CharField(max_length=1, blank=True, null=True)
    blockce20 = models.CharField(max_length=4, blank=True, null=True)
    countyfp20 = models.CharField(max_length=3, blank=True, null=True)
    statefp20 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faces'


class Featnames(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    predirabrv = models.CharField(max_length=15, blank=True, null=True)
    pretypabrv = models.CharField(max_length=50, blank=True, null=True)
    prequalabr = models.CharField(max_length=15, blank=True, null=True)
    sufdirabrv = models.CharField(max_length=15, blank=True, null=True)
    suftypabrv = models.CharField(max_length=50, blank=True, null=True)
    sufqualabr = models.CharField(max_length=15, blank=True, null=True)
    predir = models.CharField(max_length=2, blank=True, null=True)
    pretyp = models.CharField(max_length=3, blank=True, null=True)
    prequal = models.CharField(max_length=2, blank=True, null=True)
    sufdir = models.CharField(max_length=2, blank=True, null=True)
    suftyp = models.CharField(max_length=3, blank=True, null=True)
    sufqual = models.CharField(max_length=2, blank=True, null=True)
    linearid = models.CharField(max_length=22, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    paflag = models.CharField(max_length=1, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'featnames'


class GeocodeSettings(models.Model):
    name = models.TextField(primary_key=True)
    setting = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocode_settings'


class GeocodeSettingsDefault(models.Model):
    name = models.TextField(primary_key=True)
    setting = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocode_settings_default'


class Institucion(models.Model):
    id_i = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=150)
    direccion = models.CharField(max_length=200)
    #setColores = models.CharField(max_length=200)
    logo = models.CharField(max_length=255, blank=True, null=True)
    e_validacion = models.TextField()  # This field type is a guess.
    estado = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'institucion'


class Layer(models.Model):
    pk = models.CompositePrimaryKey('topology_id', 'layer_id')
    topology = models.ForeignKey('Topology', models.DO_NOTHING)
    layer_id = models.IntegerField()
    schema_name = models.CharField()
    table_name = models.CharField()
    feature_column = models.CharField()
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('schema_name', 'table_name', 'feature_column'),)


class LoaderLookuptables(models.Model):
    process_order = models.IntegerField()
    lookup_name = models.TextField(primary_key=True, db_comment='This is the table name to inherit from and suffix of resulting output table -- how the table will be named --  edges here would mean -- ma_edges , pa_edges etc. except in the case of national tables. national level tables have no prefix')
    table_name = models.TextField(blank=True, null=True, db_comment='suffix of the tables to load e.g.  edges would load all tables like *edges.dbf(shp)  -- so tl_2010_42129_edges.dbf .  ')
    single_mode = models.BooleanField()
    load = models.BooleanField(db_comment="Whether or not to load the table.  For states and zcta5 (you may just want to download states10, zcta510 nationwide file manually) load your own into a single table that inherits from tiger.states, tiger.zcta5.  You'll get improved performance for some geocoding cases.")
    level_county = models.BooleanField()
    level_state = models.BooleanField()
    level_nation = models.BooleanField(db_comment='These are tables that contain all data for the whole US so there is just a single file')
    post_load_process = models.TextField(blank=True, null=True)
    single_geom_mode = models.BooleanField(blank=True, null=True)
    insert_mode = models.CharField(max_length=1)
    pre_load_process = models.TextField(blank=True, null=True)
    columns_exclude = models.TextField(blank=True, null=True, db_comment='List of columns to exclude as an array. This is excluded from both input table and output table and rest of columns remaining are assumed to be in same order in both tables. gid, geoid,cpi,suffix1ce are excluded if no columns are specified.')  # This field type is a guess.
    website_root_override = models.TextField(blank=True, null=True, db_comment='Path to use for wget instead of that specified in year table.  Needed currently for zcta where they release that only for 2000 and 2010')

    class Meta:
        managed = False
        db_table = 'loader_lookuptables'


class LoaderPlatform(models.Model):
    os = models.CharField(primary_key=True, max_length=50)
    declare_sect = models.TextField(blank=True, null=True)
    pgbin = models.TextField(blank=True, null=True)
    wget = models.TextField(blank=True, null=True)
    unzip_command = models.TextField(blank=True, null=True)
    psql = models.TextField(blank=True, null=True)
    path_sep = models.TextField(blank=True, null=True)
    loader = models.TextField(blank=True, null=True)
    environ_set_command = models.TextField(blank=True, null=True)
    county_process_command = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_platform'


class LoaderVariables(models.Model):
    tiger_year = models.CharField(primary_key=True, max_length=4)
    website_root = models.TextField(blank=True, null=True)
    staging_fold = models.TextField(blank=True, null=True)
    data_schema = models.TextField(blank=True, null=True)
    staging_schema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_variables'


class PagcGaz(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    stdword = models.TextField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_gaz'


class PagcLex(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    stdword = models.TextField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_lex'


class PagcRules(models.Model):
    rule = models.TextField(blank=True, null=True)
    is_custom = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagc_rules'


class Place(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    placefp = models.CharField(max_length=5, blank=True, null=True)
    placens = models.CharField(max_length=8, blank=True, null=True)
    plcidfp = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    cpi = models.CharField(max_length=1, blank=True, null=True)
    pcicbsa = models.CharField(max_length=1, blank=True, null=True)
    pcinecta = models.CharField(max_length=1, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.BigIntegerField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'place'


class PlaceLookup(models.Model):
    pk = models.CompositePrimaryKey('st_code', 'pl_code')
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True, null=True)
    pl_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_lookup'


class SecondaryUnitLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secondary_unit_lookup'


class Sensor(models.Model):
    id_sen = models.AutoField(primary_key=True)
    id_e = models.ForeignKey(Estacion, models.DO_NOTHING, db_column='id_e')
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    api_key = models.CharField(max_length=64, blank=True, null=True)
    estado = models.TextField()  # This field type is a guess.
    fecha_alta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sensor'


class SensorVariable(models.Model):
    pk = models.CompositePrimaryKey('id_sen', 'id_var', 'tiempo')
    id_sen = models.ForeignKey(Sensor, models.DO_NOTHING, db_column='id_sen')
    id_var = models.ForeignKey('Variable', models.DO_NOTHING, db_column='id_var')
    tiempo = models.DateTimeField()
    valor = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'sensor_variable'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class State(models.Model):
    gid = models.IntegerField(unique=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    division = models.CharField(max_length=2, blank=True, null=True)
    statefp = models.CharField(primary_key=True, max_length=2)
    statens = models.CharField(max_length=8, blank=True, null=True)
    stusps = models.CharField(unique=True, max_length=2)
    name = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.BigIntegerField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'state'


class StateLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=40, blank=True, null=True)
    abbrev = models.CharField(unique=True, max_length=3, blank=True, null=True)
    statefp = models.CharField(unique=True, max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_lookup'


class StreetTypeLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    abbrev = models.CharField(max_length=50, blank=True, null=True)
    is_hw = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'street_type_lookup'


class Tabblock(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blockce = models.CharField(max_length=4, blank=True, null=True)
    tabblock_id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=20, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    ur = models.CharField(max_length=1, blank=True, null=True)
    uace = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tabblock'


class Tabblock20(models.Model):
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blockce = models.CharField(max_length=4, blank=True, null=True)
    geoid = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=10, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    ur = models.CharField(max_length=1, blank=True, null=True)
    uace = models.CharField(max_length=5, blank=True, null=True)
    uatype = models.CharField(max_length=1, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    housing = models.FloatField(blank=True, null=True)
    pop = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabblock20'


class Topology(models.Model):
    name = models.CharField(unique=True)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'


class Tract(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    tract_id = models.CharField(primary_key=True, max_length=11)
    name = models.CharField(max_length=7, blank=True, null=True)
    namelsad = models.CharField(max_length=20, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tract'


class Usuario(models.Model):
    id_u = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(unique=True, max_length=120)
    contrasena = models.CharField(max_length=120)
    estado = models.TextField()  # This field type is a guess.
    fecha_reg = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioEstacion(models.Model):
    pk = models.CompositePrimaryKey('id_u', 'id_e', 'inicio')
    id_u = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_u')
    id_e = models.ForeignKey(Estacion, models.DO_NOTHING, db_column='id_e')
    rol_estacion = models.TextField()  # This field type is a guess.
    inicio = models.DateTimeField()
    final = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_estacion'


class UsuarioInstitucion(models.Model):
    pk = models.CompositePrimaryKey('id_i', 'id_u')
    id_i = models.ForeignKey(Institucion, models.DO_NOTHING, db_column='id_i')
    id_u = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_u')
    rol = models.TextField()  # This field type is a guess.
    e_validacion = models.TextField()  # This field type is a guess.
    fecha_asignado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'usuario_institucion'


class Variable(models.Model):
    id_var = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_variable = models.TextField()  # This field type is a guess.
    unidad = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variable'


class Zcta5(models.Model):
    pk = models.CompositePrimaryKey('zcta5ce', 'statefp')
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2)
    zcta5ce = models.CharField(max_length=5)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    partflg = models.CharField(max_length=1, blank=True, null=True)
    the_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'zcta5'


class ZipLookup(models.Model):
    zip = models.IntegerField(primary_key=True)
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField(blank=True, null=True)
    cousub = models.CharField(max_length=90, blank=True, null=True)
    pl_code = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=90, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup'


class ZipLookupAll(models.Model):
    zip = models.IntegerField(blank=True, null=True)
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField(blank=True, null=True)
    cousub = models.CharField(max_length=90, blank=True, null=True)
    pl_code = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=90, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup_all'


class ZipLookupBase(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)
    state = models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    city = models.CharField(max_length=90, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup_base'


class ZipState(models.Model):
    pk = models.CompositePrimaryKey('zip', 'stusps')
    zip = models.CharField(max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_state'


class ZipStateLoc(models.Model):
    pk = models.CompositePrimaryKey('zip', 'stusps', 'place')
    zip = models.CharField(max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    place = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'zip_state_loc'
